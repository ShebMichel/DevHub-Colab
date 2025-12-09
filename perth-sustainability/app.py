from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, date
import io, csv
import pandas as pd


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sustainability.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-key'
db = SQLAlchemy(app)

# ----------------------
# Models
# ----------------------
class Household(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class UsageEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    household_id = db.Column(db.Integer, db.ForeignKey('household.id'), nullable=False)
    entry_type = db.Column(db.String(20), nullable=False)  # 'water' or 'energy'
    value = db.Column(db.Float, nullable=False)  # litres for water, kWh for energy
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

    household = db.relationship('Household', backref=db.backref('entries', lazy=True))

# ----------------------
# Example bin schedule mapping (simplified)
# ----------------------
BIN_SCHEDULES = {
    '6000': ('Monday', 'Wednesday'),
    '6001': ('Tuesday', 'Thursday'),
    '6002': ('Wednesday', 'Friday'),
    '6003': ('Thursday', 'Monday'),
    'default': ('Friday', 'Tuesday'),
}

def get_simple_bin_schedule(postcode):
    prefix = postcode.strip().replace(' ', '')[:4]
    sched = BIN_SCHEDULES.get(prefix, BIN_SCHEDULES['default'])
    return {'general': sched[0], 'recycling': sched[1]}

# ----------------------
# Utilities: Green score & tips
# ----------------------
def compute_green_score(household):
    entries = UsageEntry.query.filter_by(household_id=household.id).all()
    if not entries:
        return 50

    df = pd.DataFrame([{
        'type': e.entry_type,
        'value': e.value,
        'date': e.recorded_at.date()
    } for e in entries])

    today = date.today()
    window_start = today - timedelta(days=30)
    df_recent = df[df['date'] >= window_start]

    water_baseline = 200.0
    energy_baseline = 20.0

    water_score = 50.0
    energy_score = 50.0
    
    if not df_recent.empty:
        if 'water' in df_recent['type'].values:
            w = df_recent[df_recent['type']=='water'].groupby('date')['value'].sum()
            if not w.empty:
                avg_w = w.mean()
                water_score = max(0, min(100, (1 - (avg_w / water_baseline)) * 100 + 50))
        if 'energy' in df_recent['type'].values:
            e = df_recent[df_recent['type']=='energy'].groupby('date')['value'].sum()
            if not e.empty:
                avg_e = e.mean()
                energy_score = max(0, min(100, (1 - (avg_e / energy_baseline)) * 100 + 50))

    score = 0.5 * energy_score + 0.5 * water_score
    return int(score)

def generate_tips(household, green_score):
    tips = []
    if green_score < 30:
        tips.append("Your score is low — consider an energy audit and reduce standby power (unplug chargers and unused devices).")
        tips.append("Install low-flow shower heads and check for leaks to reduce water usage.")
    elif green_score < 60:
        tips.append("Good start — replace old incandescent bulbs with LED and run full loads in washing/dishwasher.")
        tips.append("Track shower times and set a family challenge to save water each week.")
    else:
        tips.append("Great job! Keep monitoring and consider solar panels or a rainwater tank for further gains.")
        tips.append("Share your habits with neighbours and start a community swap or tool library.")

    schedule = get_simple_bin_schedule(household.postcode)
    tips.append(f"General waste day: {schedule['general']}. Recycling day: {schedule['recycling']}.")
    return tips

# ----------------------
# Routes
# ----------------------
@app.route('/')
def index():
    households = Household.query.order_by(Household.created_at.desc()).all()
    return render_template('index.html', households=households)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()
        postcode = request.form['postcode'].strip()
        if not name or not postcode:
            flash('Please provide both a name and postcode.', 'danger')
            return redirect(url_for('register'))
        hh = Household(name=name, postcode=postcode)
        db.session.add(hh)
        db.session.commit()
        flash('Household added! You can now add usage or view the dashboard.', 'success')
        return redirect(url_for('dashboard', household_id=hh.id))
    return render_template('register.html')

@app.route('/household/<int:household_id>')
def dashboard(household_id):
    hh = Household.query.get_or_404(household_id)
    entries = UsageEntry.query.filter_by(household_id=household_id).order_by(UsageEntry.recorded_at.desc()).limit(50).all()
    green_score = compute_green_score(hh)
    tips = generate_tips(hh, green_score)
    schedule = get_simple_bin_schedule(hh.postcode)
    
    df = pd.DataFrame([{
        'type': e.entry_type,
        'value': e.value,
        'date': e.recorded_at.strftime('%Y-%m-%d')
    } for e in entries])
    
    recent_summary = {}
    if not df.empty:
        recent_summary = df.groupby('type')['value'].sum().to_dict()
    
    return render_template('dashboard.html', household=hh, entries=entries, 
                         green_score=green_score, tips=tips, schedule=schedule, 
                         recent_summary=recent_summary)

@app.route('/household/<int:household_id>/add', methods=['GET', 'POST'])
def add_usage(household_id):
    hh = Household.query.get_or_404(household_id)
    if request.method == 'POST':
        entry_type = request.form['entry_type']
        value = request.form['value']
        recorded_at = request.form.get('recorded_at', '')
        try:
            value = float(value)
            if recorded_at:
                recorded_dt = datetime.fromisoformat(recorded_at)
            else:
                recorded_dt = datetime.utcnow()
            entry = UsageEntry(household_id=household_id, entry_type=entry_type, 
                             value=value, recorded_at=recorded_dt)
            db.session.add(entry)
            db.session.commit()
            flash('Entry added', 'success')
            return redirect(url_for('dashboard', household_id=household_id))
        except Exception as e:
            flash(f'Invalid input: {e}', 'danger')
            return redirect(url_for('add_usage', household_id=household_id))

    return render_template('add_usage.html', household=hh)

@app.route('/export/<int:household_id>')
def export_csv(household_id):
    hh = Household.query.get_or_404(household_id)
    entries = UsageEntry.query.filter_by(household_id=household_id).order_by(UsageEntry.recorded_at).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['id','entry_type','value','recorded_at'])
    for e in entries:
        writer.writerow([e.id, e.entry_type, e.value, e.recorded_at.isoformat()])
    output.seek(0)
    mem = io.BytesIO()
    mem.write(output.getvalue().encode('utf-8'))
    mem.seek(0)
    filename = f"{hh.name.replace(' ', '_')}_usage.csv"
    return send_file(mem, as_attachment=True, download_name=filename, mimetype='text/csv')

@app.route('/import/<int:household_id>', methods=['GET','POST'])
def import_csv(household_id):
    hh = Household.query.get_or_404(household_id)
    if request.method == 'POST':
        f = request.files.get('file')
        if not f:
            flash('No file uploaded', 'danger')
            return redirect(url_for('import_csv', household_id=household_id))
        try:
            df = pd.read_csv(f)
            for _, row in df.iterrows():
                entry_type = row.get('entry_type', '').strip()
                value = float(row.get('value', 0))
                recorded_at = row.get('recorded_at', '')
                if pd.isna(recorded_at) or recorded_at == '':
                    recorded_dt = datetime.utcnow()
                else:
                    recorded_dt = datetime.fromisoformat(str(recorded_at))
                entry = UsageEntry(household_id=household_id, entry_type=entry_type, 
                                 value=value, recorded_at=recorded_dt)
                db.session.add(entry)
            db.session.commit()
            flash('Imported usage entries', 'success')
        except Exception as e:
            flash(f'Import failed: {e}', 'danger')
        return redirect(url_for('dashboard', household_id=household_id))
    return render_template('import_export.html', household=hh)

# Simple API endpoints
@app.route('/api/households', methods=['GET','POST'])
def api_households():
    if request.method == 'GET':
        hhs = Household.query.all()
        return {'households': [{'id':h.id,'name':h.name,'postcode':h.postcode} for h in hhs]}
    else:
        data = request.get_json()
        name = data.get('name')
        postcode = data.get('postcode')
        if not name or not postcode:
            return {'error':'name and postcode required'}, 400
        hh = Household(name=name, postcode=postcode)
        db.session.add(hh)
        db.session.commit()
        return {'id': hh.id, 'name': hh.name, 'postcode': hh.postcode}, 201

@app.route('/api/household/<int:household_id>/usage', methods=['POST'])
def api_add_usage(household_id):
    hh = Household.query.get_or_404(household_id)
    data = request.get_json()
    entry_type = data.get('entry_type')
    value = data.get('value')
    if entry_type not in ('water','energy'):
        return {'error':'entry_type must be "water" or "energy"'}, 400
    try:
        value = float(value)
    except:
        return {'error':'value must be numeric'}, 400
    entry = UsageEntry(household_id=household_id, entry_type=entry_type, value=value)
    db.session.add(entry)
    db.session.commit()
    return {'status':'ok','entry_id':entry.id}, 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)