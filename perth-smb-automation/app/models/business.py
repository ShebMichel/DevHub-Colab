from datetime import datetime
from app import db

class Business(db.Model):
    __tablename__ = 'businesses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    business_type = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    subscription_tier = db.Column(db.String(50), default='basic')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    appointments = db.relationship('Appointment', backref='business', lazy=True, cascade='all, delete-orphan')
    customers = db.relationship('Customer', backref='business', lazy=True, cascade='all, delete-orphan')
    inventory = db.relationship('Inventory', backref='business', lazy=True, cascade='all, delete-orphan')
    notifications = db.relationship('Notification', backref='business', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.business_type,
            'phone': self.phone,
            'email': self.email,
            'subscription_tier': self.subscription_tier,
            'created_at': self.created_at.isoformat()
        }