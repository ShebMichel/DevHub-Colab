from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "devcolab-secret-key"

DATA_FILE = "events.json"


# ---------- Utility functions ----------

def load_events():
    try:
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print("Error loading events:", e)
        return []


def save_events(events):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(events, f, indent=2)
    except IOError as e:
        print("Error saving events:", e)
        raise


# ---------- Routes ----------

@app.route("/", methods=["GET"])
def index():
    category = request.args.get("category", "All")
    events = load_events()

    if category != "All":
        events = [e for e in events if e["category"] == category]

    return render_template("index.html", events=events, category=category)


@app.route("/add", methods=["POST"])
def add_event():
    try:
        name = request.form.get("name", "").strip()
        date = request.form.get("date", "")
        category = request.form.get("category", "")

        # Validation
        if not name or not date or not category:
            flash("❌ All fields are required.", "error")
            return redirect(url_for("index"))

        # Validate date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            flash("❌ Invalid date format.", "error")
            return redirect(url_for("index"))

        events = load_events()

        new_event = {
            "id": int(datetime.now().timestamp()),
            "name": name,
            "date": date,
            "category": category
        }

        events.append(new_event)
        save_events(events)

        flash("✅ Event added successfully!", "success")

    except Exception as e:
        print("Unexpected error:", e)
        flash("⚠️ Something went wrong. Please try again.", "error")

    return redirect(url_for("index"))


# ---------- App runner ----------

if __name__ == "__main__":
    app.run(debug=True)
