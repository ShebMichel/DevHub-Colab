from datetime import datetime
from app import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    notification_type = db.Column(db.String(50))
    message = db.Column(db.Text)
    channel = db.Column(db.String(20))  # SMS or Email
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='sent')
    
    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'type': self.notification_type,
            'message': self.message,
            'channel': self.channel,
            'timestamp': self.timestamp.isoformat(),
            'status': self.status
        }