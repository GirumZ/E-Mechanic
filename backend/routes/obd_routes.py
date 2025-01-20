from flask import Blueprint, jsonify, request
from app import db
from models import OBDCode

obd_bp = Blueprint('obd', __name__, url_prefix='/api/obd')

# Fetch all OBD codes
@obd_bp.route('/', methods=['GET'])
def get_all_obd_codes():
    obd_codes = OBDCode.query.all()
    return jsonify([{
        'id': obd_code.obd_id,
        'code': obd_code.obd_code,
        'description': obd_code.obd_description
    } for obd_code in obd_codes])

# Fetch a specific OBD code by ID
@obd_bp.route('/<int:obd_id>', methods=['GET'])
def get_obd_code_by_id(obd_id):
    obd_code = OBDCode.query.get_or_404(obd_id)
    return jsonify({
        'id': obd_code.obd_id,
        'code': obd_code.obd_code,
        'description': obd_code.obd_description
    })

# Fetch a specific OBD code by code string
@obd_bp.route('/code/<string:obd_code>', methods=['GET'])
def get_obd_code_by_code(obd_code):
    obd_code = OBDCode.query.filter_by(obd_code=obd_code).first_or_404()
    return jsonify({
        'id': obd_code.obd_id,
        'code': obd_code.obd_code,
        'description': obd_code.obd_description
    })

# Create a new OBD code
@obd_bp.route('/', methods=['POST'])
def create_obd_code():
    data = request.json
    new_obd_code = OBDCode(
        code=data['obd_code'],
        description=data['obd_description']
    )
    db.session.add(new_obd_code)
    db.session.commit()
    return jsonify({"message": "OBD code created successfully", "id": new_obd_code.id}), 201

# Update an OBD code
@obd_bp.route('/<int:obd_id>', methods=['PUT'])
def update_obd_code(obd_id):
    data = request.json
    obd_code = OBDCode.query.get_or_404(obd_id)
    obd_code.code = data['obd_code']
    obd_code.description = data['obd_description']
    db.session.commit()
    return jsonify({"message": "OBD code updated successfully"})

# Delete an OBD code
@obd_bp.route('/<int:obd_id>', methods=['DELETE'])
def delete_obd_code(obd_id):
    obd_code = OBDCode.query.get_or_404(obd_id)
    db.session.delete(obd_code)
    db.session.commit()
    return jsonify({"message": "OBD code deleted successfully"})
