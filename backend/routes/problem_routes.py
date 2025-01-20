from flask import Blueprint, jsonify, request
from app import db
from models import Problem

problem_bp = Blueprint('problem', __name__, url_prefix='/api/problems')

# Fetch all problems
@problem_bp.route('/', methods=['GET'])
def get_all_problems():
    problems = Problem.query.all()
    return jsonify([{
        'id': problem.problem_id,
        'problem_description': problem.problem_description,
        'question_id': problem.question_id
    } for problem in problems])

# Fetch a specific problem by ID
@problem_bp.route('/<int:problem_id>', methods=['GET'])
def get_problem_by_id(problem_id):
    problem = Problem.query.get_or_404(problem_id)
    return jsonify({
        'id': problem.problem_id,
        'problem_description': problem.problem_description,
        'question_id': problem.question_id
    })

# Fetch problems by Question ID
@problem_bp.route('/question/<int:question_id>', methods=['GET'])
def get_problems_by_question(question_id):
    problems = Problem.query.filter_by(question_id=question_id).all()
    return jsonify([{
        'id': problem.problem_id,
        'problem_description': problem.problem_description,
        'question_id': problem.question_id
    } for problem in problems])

# Create a new problem
@problem_bp.route('/', methods=['POST'])
def create_problem():
    data = request.json
    new_problem = Problem(
        problem_description=data['problem_description'],
        question_id=data['question_id']
    )
    db.session.add(new_problem)
    db.session.commit()
    return jsonify({"message": "Problem created successfully", "id": new_problem.id}), 201

# Update a problem
@problem_bp.route('/<int:problem_id>', methods=['PUT'])
def update_problem(problem_id):
    data = request.json
    problem = Problem.query.get_or_404(problem_id)
    problem.problem_description = data['problem_description']
    problem.question_id = data['question_id']
    db.session.commit()
    return jsonify({"message": "Problem updated successfully"})

# Delete a problem
@problem_bp.route('/<int:problem_id>', methods=['DELETE'])
def delete_problem(problem_id):
    problem = Problem.query.get_or_404(problem_id)
    db.session.delete(problem)
    db.session.commit()
    return jsonify({"message": "Problem deleted successfully"})
