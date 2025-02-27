from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# Ensure the folder exists
os.makedirs("rego_data", exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is inside templates folder

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone = request.form.get('phone')
    reason = request.form.get('reason')

    # Create a DataFrame
    data = pd.DataFrame([[first_name, last_name, phone, reason]],
                         columns=["First Name", "Last Name", "Phone", "Reason"])

    file_path = "rego_data/visitor_data.xlsx"

    # Append data to Excel file
    if os.path.exists(file_path):
        existing_data = pd.read_excel(file_path)
        updated_data = pd.concat([existing_data, data], ignore_index=True)
    else:
        updated_data = data

    updated_data.to_excel(file_path, index=False)

    return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)
