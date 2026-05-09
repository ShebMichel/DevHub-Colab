from datetime import datetime
from app import db

class Inventory(db.Model):
    __tablename__ = 'inventory'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    item_name = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    min_stock = db.Column(db.Integer, default=10)
    unit = db.Column(db.String(50), default='pieces')
    cost = db.Column(db.Float, default=0.0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'name': self.item_name,
            'quantity': self.quantity,
            'min_stock': self.min_stock,
            'unit': self.unit,
            'cost': self.cost,
            'is_low_stock': self.quantity <= self.min_stock
        }