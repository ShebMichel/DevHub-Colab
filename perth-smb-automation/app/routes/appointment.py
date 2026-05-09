from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from app.models import Appointment
from app.services.reminder_service import send_appointment_reminder

bp = Blueprint('appointment', __name__, url_prefix='/api')

@bp.route('/businesses/<int:business_id>/appointments', methods=['GET'])
def get_appointments(business_id):
    appointments = Appointment.query.filter_by(business_id=business_id).all()
    return jsonify([a.to_dict() for a in appointments])

@bp.route('/appointments', methods=['POST'])
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
    return jsonify(appointment.to_dict()), 201

@bp.route('/appointments/<int:appointment_id>', methods=['GET', 'PUT', 'DELETE'])
def appointment_detail(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    
    if request.method == 'GET':
        return jsonify(appointment.to_dict())
    
    if request.method == 'DELETE':
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted'})
    
    if request.method == 'PUT':
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
        return jsonify(appointment.to_dict())

@bp.route('/appointments/<int:appointment_id>/send-reminder', methods=['POST'])
def send_reminder(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    success, message = send_appointment_reminder(appointment)
    
    if success:
        return jsonify({'message': 'Reminder sent', 'details': message})
    return jsonify({'error': 'Failed to send reminder', 'details': message}), 500