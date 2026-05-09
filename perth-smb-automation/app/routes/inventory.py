from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from app.models import Inventory

bp = Blueprint('inventory', __name__, url_prefix='/api')

@bp.route('/businesses/<int:business_id>/inventory', methods=['GET'])
def get_inventory(business_id):
    inventory = Inventory.query.filter_by(business_id=business_id).all()
    return jsonify([i.to_dict() for i in inventory])

@bp.route('/inventory', methods=['POST'])
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
    return jsonify(item.to_dict()), 201

@bp.route('/inventory/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def inventory_detail(item_id):
    item = Inventory.query.get_or_404(item_id)
    
    if request.method == 'GET':
        return jsonify(item.to_dict())
    
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Inventory item deleted'})
    
    if request.method == 'PUT':
        data = request.json
        item.item_name = data.get('name', item.item_name)
        item.quantity = data.get('quantity', item.quantity)
        item.min_stock = data.get('min_stock', item.min_stock)
        item.unit = data.get('unit', item.unit)
        item.cost = data.get('cost', item.cost)
        item.last_updated = datetime.utcnow()
        db.session.commit()
        return jsonify(item.to_dict())