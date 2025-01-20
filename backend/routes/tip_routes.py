from flask import Blueprint, jsonify, request
from app import db
from models import Tip


tip_pb = Blueprint('tip', __name__, url_prefix='/api/tips')

# Fetch all tips
@tip_pb.route('/', methods=['GET'])
def get_all_tips():
    tips = Tip.query.all()
    return jsonify([{
        'id': tip.tip_id,
        'tip_short': tip.tip_short,
        'tip_long' : tip.tip_long
    } for tip in tips])

# Fetch a specific tip by ID
@tip_pb.route('/<int:tip_id>', methods=['GET'])
def get_tip_by_id(tip_id):
    tip = Tip.query.get_or_404(tip_id)
    return jsonify({
        'id': tip.tip_id,
        'tip_short': tip.tip_short,
        'tip_long' : tip.tip_long
    })

# Create a new tip
@tip_pb.route('/', methods=['POST'])
def create_tip():
    data = request.json
    new_tip = Tip(tip_short=data['tip_short'])
    db.session.add(new_tip)
    db.session.commit()
    return jsonify({"message": "Tip created successfully", "id": new_tip.id}), 201

# Update a tip
@tip_pb.route('/<int:tip_id>', methods=['PUT'])
def update_tip(tip_id):
    data = request.json
    tip = Tip.query.get_or_404(tip_id)
    tip.tip_short = data['tip_short']
    tip.tip_long = data['tip_long']
    db.session.commit()
    return jsonify({"message": "Tip updated successfully"})

# Delete a tip
@tip_pb.route('/<int:tip_id>', methods=['DELETE'])
def delete_tip(tip_id):
    tip = Tip.query.get_or_404(tip_id)
    db.session.delete(tip)
    db.session.commit()
    return jsonify({"message": "Tip deleted successfully"})
