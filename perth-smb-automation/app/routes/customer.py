from flask import Blueprint, request, jsonify
from app import db
from app.models import Customer

bp = Blueprint('customer', __name__, url_prefix='/api')

@bp.route('/businesses/<int:business_id>/customers', methods=['GET'])
def get_customers(business_id):
    customers = Customer.query.filter_by(business_id=business_id).all()
    return jsonify([c.to_dict() for c in customers])

@bp.route('/customers', methods=['POST'])
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
    return jsonify(customer.to_dict()), 201

@bp.route('/customers/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def customer_detail(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    
    if request.method == 'GET':
        return jsonify(customer.to_dict())
    
    if request.method == 'DELETE':
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted'})
    
    if request.method == 'PUT':
        data = request.json
        customer.name = data.get('name', customer.name)
        customer.phone = data.get('phone', customer.phone)
        customer.email = data.get('email', customer.email)
        db.session.commit()
        return jsonify(customer.to_dict())