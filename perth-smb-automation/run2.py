# Perth SMB Automation System - Complete Python Backend
# Flask API with SQLite, SMS/Email automation, and scheduler

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import os
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///perth_smb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
CORS(app)
db = SQLAlchemy(app)

# Configuration for SMS/Email (set as environment variables)
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', 'your_twilio_sid')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', 'your_twilio_token')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER', '+61412345678')
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
SMTP_EMAIL = os.environ.get('SMTP_EMAIL', 'your-email@gmail.com')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', 'your-app-password')

# ==================== DATABASE MODELS ====================

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    business_type = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    subscription_tier = db.Column(db.String(50), default='basic')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    appointments = db.relationship('Appointment', backref='business', lazy=True)
    customers = db.relationship('Customer', backref='business', lazy=True)
    inventory = db.relationship('Inventory', backref='business', lazy=True)
    notifications = db.relationship('Notification', backref='business', lazy=True)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    total_spent = db.Column(db.Float, default=0.0)
    visits = db.Column(db.Integer, default=0)
    last_visit = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    appointments = db.relationship('Appointment', backref='customer', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    service = db.Column(db.String(200), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(50), default='pending')
    price = db.Column(db.Float, default=0.0)
    reminder_sent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    item_name = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    min_stock = db.Column(db.Integer, default=10)
    unit = db.Column(db.String(50), default='pieces')
    cost = db.Column(db.Float, default=0.0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    notification_type = db.Column(db.String(50))
    message = db.Column(db.Text)
    channel = db.Column(db.String(20))  # SMS or Email
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='sent')

# ==================== HELPER FUNCTIONS ====================

def send_sms(to_phone, message):
    """Send SMS using Twilio"""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone
        )
        return True, message.sid
    except Exception as e:
        print(f"SMS Error: {str(e)}")
        return False, str(e)

def send_email(to_email, subject, body):
    """Send Email using SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True, "Email sent"
    except Exception as e:
        print(f"Email Error: {str(e)}")
        return False, str(e)

def check_and_send_reminders():
    """Check for appointments in next 24 hours and send reminders"""
    with app.app_context():
        tomorrow = datetime.now() + timedelta(hours=24)
        today = datetime.now()
        
        appointments = Appointment.query.filter(
            Appointment.reminder_sent == False,
            Appointment.status == 'confirmed'
        ).all()
        
        for apt in appointments:
            apt_datetime = datetime.combine(apt.appointment_date, apt.appointment_time)
            hours_until = (apt_datetime - datetime.now()).total_seconds() / 3600
            
            if 0 < hours_until <= 24:
                customer = Customer.query.get(apt.customer_id)
                business = Business.query.get(apt.business_id)
                
                message = f"Reminder: Your appointment for {apt.service} is tomorrow at {apt.appointment_time.strftime('%I:%M %p')} with {business.name}. See you soon!"
                
                # Send SMS
                success, result = send_sms(customer.phone, message)
                
                if success:
                    apt.reminder_sent = True
                    
                    # Log notification
                    notif = Notification(
                        business_id=business.id,
                        notification_type='reminder',
                        message=f"Reminder sent to {customer.name} for {apt.service}",
                        channel='SMS'
                    )
                    db.session.add(notif)
                    db.session.commit()
                    print(f"Reminder sent to {customer.name}")

def check_low_stock():
    """Check inventory for low stock items"""
    with app.app_context():
        low_stock_items = Inventory.query.filter(
            Inventory.quantity <= Inventory.min_stock
        ).all()
        
        for item in low_stock_items:
            business = Business.query.get(item.business_id)
            message = f"Low Stock Alert: {item.item_name} - Only {item.quantity} {item.unit} left!"
            
            # Log notification
            notif = Notification(
                business_id=business.id,
                notification_type='low_stock',
                message=message,
                channel='Email'
            )
            db.session.add(notif)
        
        if low_stock_items:
            db.session.commit()

# ==================== API ROUTES ====================

@app.route('/')
def index():
    """Main dashboard route"""
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Perth SMB Automation API</title>
        <style>
            body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #2563eb; }
            .endpoint { background: #f3f4f6; padding: 15px; margin: 10px 0; border-radius: 5px; }
            .method { color: #059669; font-weight: bold; }
            code { background: #e5e7eb; padding: 2px 6px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <h1>🚀 Perth SMB Automation API</h1>
        <p>Flask-based automation system for Perth small businesses</p>
        
        <h2>📡 API Endpoints</h2>
        
        <div class="endpoint">
            <span class="method">GET</span> <code>/api/businesses</code> - List all businesses
        </div>
        
        <div class="endpoint">
            <span class="method">POST</span> <code>/api/businesses</code> - Create new business
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <code>/api/businesses/&lt;id&gt;/appointments</code> - Get appointments
        </div>
        
        <div class="endpoint">
            <span class="method">POST</span> <code>/api/appointments</code> - Create appointment
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <code>/api/businesses/&lt;id&gt;/customers</code> - Get customers
        </div>
        
        <div class="endpoint">
            <span class="method">POST</span> <code>/api/customers</code> - Create customer
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <code>/api/businesses/&lt;id&gt;/inventory</code> - Get inventory
        </div>
        
        <div class="endpoint">
            <span class="method">POST</span> <code>/api/inventory</code> - Create inventory item
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <code>/api/businesses/&lt;id&gt;/notifications</code> - Get notifications
        </div>
        
        <div class="endpoint">
            <span class="method">POST</span> <code>/api/reminders/send/&lt;appointment_id&gt;</code> - Send manual reminder
        </div>
        
        <h2>✨ Features</h2>
        <ul>
            <li>✅ Automatic 24-hour appointment reminders</li>
            <li>✅ Low stock alerts</li>
            <li>✅ SMS & Email notifications</li>
            <li>✅ Customer relationship management</li>
            <li>✅ Inventory tracking</li>
        </ul>
        
        <p><strong>Status:</strong> <span style="color: green;">● Running</span></p>
    </body>
    </html>
    """)

# Business Routes
@app.route('/api/businesses', methods=['GET', 'POST'])
def businesses():
    if request.method == 'POST':
        data = request.json
        business = Business(
            name=data['name'],
            business_type=data.get('business_type'),
            phone=data.get('phone'),
            email=data.get('email'),
            subscription_tier=data.get('subscription_tier', 'basic')
        )
        db.session.add(business)
        db.session.commit()
        return jsonify({'id': business.id, 'message': 'Business created'}), 201
    
    businesses = Business.query.all()
    return jsonify([{
        'id': b.id,
        'name': b.name,
        'type': b.business_type,
        'phone': b.phone,
        'email': b.email
    } for b in businesses])

# Customer Routes
@app.route('/api/businesses/<int:business_id>/customers', methods=['GET'])
def get_customers(business_id):
    customers = Customer.query.filter_by(business_id=business_id).all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'phone': c.phone,
        'email': c.email,
        'total_spent': c.total_spent,
        'visits': c.visits,
        'last_visit': str(c.last_visit) if c.last_visit else None
    } for c in customers])

@app.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.json
    customer = Customer(
        business_id=data['business_id'],
        name=data['name'],
        phone=data['phone'],
        email=data.get('email')
    )
    db.session.add(customer)
    db.session.commit()
    return jsonify({'id': customer.id, 'message': 'Customer created'}), 201

@app.route('/api/customers/<int:customer_id>', methods=['PUT', 'DELETE'])
def update_delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    
    if request.method == 'DELETE':
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted'})
    
    data = request.json
    customer.name = data.get('name', customer.name)
    customer.phone = data.get('phone', customer.phone)
    customer.email = data.get('email', customer.email)
    db.session.commit()
    return jsonify({'message': 'Customer updated'})

# Appointment Routes
@app.route('/api/businesses/<int:business_id>/appointments', methods=['GET'])
def get_appointments(business_id):
    appointments = Appointment.query.filter_by(business_id=business_id).all()
    result = []
    for a in appointments:
        customer = Customer.query.get(a.customer_id)
        result.append({
            'id': a.id,
            'customer_id': a.customer_id,
            'customer_name': customer.name,
            'customer_phone': customer.phone,
            'service': a.service,
            'date': str(a.appointment_date),
            'time': str(a.appointment_time),
            'status': a.status,
            'price': a.price,
            'reminder_sent': a.reminder_sent
        })
    return jsonify(result)

@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    appointment = Appointment(
        business_id=data['business_id'],
        customer_id=data['customer_id'],
        service=data['service'],
        appointment_date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
        appointment_time=datetime.strptime(data['time'], '%H:%M').time(),
        status=data.get('status', 'pending'),
        price=data.get('price', 0.0)
    )
    db.session.add(appointment)
    db.session.commit()
    return jsonify({'id': appointment.id, 'message': 'Appointment created'}), 201

@app.route('/api/appointments/<int:appointment_id>', methods=['PUT', 'DELETE'])
def update_delete_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    
    if request.method == 'DELETE':
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted'})
    
    data = request.json
    if 'date' in data:
        appointment.appointment_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    if 'time' in data:
        appointment.appointment_time = datetime.strptime(data['time'], '%H:%M').time()
    if 'status' in data:
        appointment.status = data['status']
    if 'price' in data:
        appointment.price = data['price']
    
    db.session.commit()
    return jsonify({'message': 'Appointment updated'})

# Manual Reminder
@app.route('/api/reminders/send/<int:appointment_id>', methods=['POST'])
def send_manual_reminder(appointment_id):
    apt = Appointment.query.get_or_404(appointment_id)
    customer = Customer.query.get(apt.customer_id)
    business = Business.query.get(apt.business_id)
    
    message = f"Reminder: Your appointment for {apt.service} is on {apt.appointment_date} at {apt.appointment_time.strftime('%I:%M %p')} with {business.name}."
    
    success, result = send_sms(customer.phone, message)
    
    if success:
        apt.reminder_sent = True
        notif = Notification(
            business_id=business.id,
            notification_type='manual_reminder',
            message=f"Manual reminder sent to {customer.name}",
            channel='SMS'
        )
        db.session.add(notif)
        db.session.commit()
        return jsonify({'message': 'Reminder sent', 'sid': result})
    
    return jsonify({'error': 'Failed to send reminder', 'details': result}), 500

# Inventory Routes
@app.route('/api/businesses/<int:business_id>/inventory', methods=['GET'])
def get_inventory(business_id):
    inventory = Inventory.query.filter_by(business_id=business_id).all()
    return jsonify([{
        'id': i.id,
        'name': i.item_name,
        'quantity': i.quantity,
        'min_stock': i.min_stock,
        'unit': i.unit,
        'cost': i.cost
    } for i in inventory])

@app.route('/api/inventory', methods=['POST'])
def create_inventory():
    data = request.json
    item = Inventory(
        business_id=data['business_id'],
        item_name=data['name'],
        quantity=data['quantity'],
        min_stock=data['min_stock'],
        unit=data['unit'],
        cost=data['cost']
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'message': 'Inventory item created'}), 201

@app.route('/api/inventory/<int:item_id>', methods=['PUT', 'DELETE'])
def update_delete_inventory(item_id):
    item = Inventory.query.get_or_404(item_id)
    
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Inventory item deleted'})
    
    data = request.json
    item.item_name = data.get('name', item.item_name)
    item.quantity = data.get('quantity', item.quantity)
    item.min_stock = data.get('min_stock', item.min_stock)
    item.unit = data.get('unit', item.unit)
    item.cost = data.get('cost', item.cost)
    item.last_updated = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Inventory updated'})

# Notifications
@app.route('/api/businesses/<int:business_id>/notifications', methods=['GET'])
def get_notifications(business_id):
    notifications = Notification.query.filter_by(business_id=business_id).order_by(Notification.timestamp.desc()).limit(50).all()
    return jsonify([{
        'id': n.id,
        'type': n.notification_type,
        'message': n.message,
        'channel': n.channel,
        'timestamp': n.timestamp.isoformat()
    } for n in notifications])

# Dashboard Stats
@app.route('/api/businesses/<int:business_id>/stats', methods=['GET'])
def get_stats(business_id):
    today = datetime.now().date()
    
    total_customers = Customer.query.filter_by(business_id=business_id).count()
    today_appointments = Appointment.query.filter_by(
        business_id=business_id,
        appointment_date=today
    ).count()
    
    total_revenue = db.session.query(db.func.sum(Appointment.price)).filter_by(
        business_id=business_id
    ).scalar() or 0
    
    low_stock = Inventory.query.filter(
        Inventory.business_id == business_id,
        Inventory.quantity <= Inventory.min_stock
    ).count()
    
    return jsonify({
        'total_customers': total_customers,
        'today_appointments': today_appointments,
        'total_revenue': total_revenue,
        'low_stock_items': low_stock
    })

# ==================== SCHEDULER ====================

scheduler = BackgroundScheduler()
scheduler.add_job(func=check_and_send_reminders, trigger="interval", minutes=15)
scheduler.add_job(func=check_low_stock, trigger="interval", hours=6)
scheduler.start()

# ==================== INITIALIZATION ====================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Create demo business if none exists
        if Business.query.count() == 0:
            demo_business = Business(
                name='Perth Plumbing Pro',
                business_type='Tradie',
                phone='0412345678',
                email='contact@perthplumbing.com.au'
            )
            db.session.add(demo_business)
            db.session.commit()
            print("Demo business created!")
    
    print("\n🚀 Perth SMB Automation Server Starting...")
    print("📡 API running at http://localhost:5000")
    print("✅ Automatic reminders active (checks every 15 minutes)")
    print("📦 Low stock checker active (checks every 6 hours)")
    
    app.run(debug=True, host='0.0.0.0', port=5000)