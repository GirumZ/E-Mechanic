from flask import Blueprint, jsonify, request
from app import db
from models import Question


question_bp = Blueprint('question', __name__, url_prefix='/api/questions')

# Fetch all questions
@question_bp.route('/', methods=['GET'])
def get_all_questions():
    questions = Question.query.all()
    return jsonify([{
        'id': question.question_id,
        'question_text': question.question_text,
        'symptom_id': question.symptom_id
    } for question in questions])

# Fetch a specific question by ID
@question_bp.route('/<int:question_id>', methods=['GET'])
def get_question_by_id(question_id):
    question = Question.query.get_or_404(question_id)
    return jsonify({
        'id': question.question_id,
        'question_text': question.question_text,
        'symptom_id': question.symptom_id
    })

# Fetch questions for a specific symptom
@question_bp.route('/symptom/<int:symptom_id>', methods=['GET'])
def get_questions_by_symptom(symptom_id):
    questions = Question.query.filter_by(symptom_id=symptom_id).all()
    return jsonify([{
        'id': question.question_id,
        'question_text': question.question_text,
        'symptom_id': question.symptom_id
    } for question in questions])

# Create a new question
@question_bp.route('/', methods=['POST'])
def create_question():
    data = request.json
    new_question = Question(
        question_text=data['question_text'],
        symptom_id=data['symptom_id']
    )
    db.session.add(new_question)
    db.session.commit()
    return jsonify({"message": "Question created successfully", "id": new_question.question_id}), 201

# Update a question
@question_bp.route('/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.json
    question = Question.query.get_or_404(question_id)
    question.question_text = data['question_text']
    question.symptom_id = data['symptom_id']
    db.session.commit()
    return jsonify({"message": "Question updated successfully"})

# Delete a question
@question_bp.route('/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return jsonify({"message": "Question deleted successfully"})
