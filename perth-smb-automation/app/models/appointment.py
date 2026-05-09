from datetime import datetime
from app import db

class Appointment(db.Model):
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    service = db.Column(db.String(200), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(50), default='pending')
    price = db.Column(db.Float, default=0.0)
    reminder_sent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'customer_id': self.customer_id,
            'customer_name': self.customer.name,
            'customer_phone': self.customer.phone,
            'service': self.service,
            'date': str(self.appointment_date),
            'time': str(self.appointment_time),
            'status': self.status,
            'price': self.price,
            'reminder_sent': self.reminder_sent
        }