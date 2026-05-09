from datetime import datetime
from app import db

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    total_spent = db.Column(db.Float, default=0.0)
    visits = db.Column(db.Integer, default=0)
    last_visit = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    appointments = db.relationship('Appointment', backref='customer', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'total_spent': self.total_spent,
            'visits': self.visits,
            'last_visit': str(self.last_visit) if self.last_visit else None
        }