from flask import Blueprint, jsonify, request
from models import Symptom
from app import db

symptom_bp = Blueprint('symptom', __name__, url_prefix='/api/symptoms')

@symptom_bp.route('/', methods=['GET'])
def get_all_symptoms():
    symptoms = Symptom.query.all()
    return jsonify([{
        'id': symptom.id,
        'symptom_text': symptom.symptom_text,
        'sensation': symptom.sensation,
        'followup_available': symptom.followup_available
    } for symptom in symptoms])

# Fetch a specific symptom by ID
@symptom_bp.route('/<int:id>', methods=['GET'])
def get_symptom_by_id(id):
    symptom = Symptom.query.get_or_404(id)
    return jsonify({
        'id': symptom.id,
        'symptom_text': symptom.symptom_text,
        'sensation': symptom.sensation,
        'followup_available': symptom.followup_available
    })

# Fetch symptoms by sensation
@symptom_bp.route('/sensation/<string:sensation>', methods=['GET'])
def get_symptoms_by_sensation(sensation):
    symptoms = Symptom.query.filter_by(sensation=sensation).all()
    return jsonify([{
        'id': symptom.id,
        'symptom_text': symptom.symptom_text,
        'sensation': symptom.sensation,
        'followup_available': symptom.followup_available
    } for symptom in symptoms])

# Fetch symptoms by follow-up availability
@symptom_bp.route('/followup/<string:available>', methods=['GET'])
def get_symptoms_by_followup(available):
    followup = available.lower() == 'true'
    symptoms = Symptom.query.filter_by(followup_available=followup).all()
    return jsonify([{
        'id': symptom.id,
        'symptom_text': symptom.symptom_text,
        'sensation': symptom.sensation,
        'followup_available': symptom.followup_available
    } for symptom in symptoms])

# Create a new symptom
@symptom_bp.route('', methods=['POST'])
def create_symptom():
    data = request.json
    new_symptom = Symptom(
        symptom_text=data['symptom_text'],
        sensation=data.get('sensation'),
        followup_available=data.get('followup_available', False)
    )
    db.session.add(new_symptom)
    db.session.commit()
    return jsonify({"message": "Symptom created successfully", "id": new_symptom.id}), 201

# Update a symptom
@symptom_bp.route('/<int:id>', methods=['PUT'])
def update_symptom(id):
    data = request.json
    symptom = Symptom.query.get_or_404(id)
    symptom.symptom_text = data['symptom_text']
    symptom.sensation = data.get('sensation')
    symptom.followup_available = data.get('followup_available', False)
    db.session.commit()
    return jsonify({"message": "Symptom updated successfully"})

# Delete a symptom
@symptom_bp.route('/<int:id>', methods=['DELETE'])
def delete_symptom(id):
    symptom = Symptom.query.get_or_404(id)
    db.session.delete(symptom)
    db.session.commit()
    return jsonify({"message": "Symptom deleted successfully"})