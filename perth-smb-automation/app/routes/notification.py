from flask import Blueprint, jsonify
from app.models import Notification

bp = Blueprint('notification', __name__, url_prefix='/api')

@bp.route('/businesses/<int:business_id>/notifications', methods=['GET'])
def get_notifications(business_id):
    notifications = Notification.query.filter_by(
        business_id=business_id
    ).order_by(Notification.timestamp.desc()).limit(50).all()
    return jsonify([n.to_dict() for n in notifications])