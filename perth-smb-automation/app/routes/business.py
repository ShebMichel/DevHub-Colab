from flask import Blueprint, request, jsonify
from app import db
from app.models import Business, Appointment, Customer, Inventory

bp = Blueprint('business', __name__, url_prefix='/api/businesses')

@bp.route('', methods=['GET', 'POST'])
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
        return jsonify(business.to_dict()), 201
    
    businesses = Business.query.all()
    return jsonify([b.to_dict() for b in businesses])

@bp.route('/<int:business_id>', methods=['GET', 'PUT', 'DELETE'])
def business_detail(business_id):
    business = Business.query.get_or_404(business_id)
    
    if request.method == 'GET':
        return jsonify(business.to_dict())
    
    if request.method == 'DELETE':
        db.session.delete(business)
        db.session.commit()
        return jsonify({'message': 'Business deleted'})
    
    if request.method == 'PUT':
        data = request.json
        business.name = data.get('name', business.name)
        business.business_type = data.get('business_type', business.business_type)
        business.phone = data.get('phone', business.phone)
        business.email = data.get('email', business.email)
        db.session.commit()
        return jsonify(business.to_dict())

@bp.route('/<int:business_id>/stats', methods=['GET'])
def business_stats(business_id):
    from datetime import datetime
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
        'total_revenue': float(total_revenue),
        'low_stock_items': low_stock
    })