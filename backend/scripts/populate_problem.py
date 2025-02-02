import csv
import os
from app import create_app
from app.extensions import db  # Import your app and db instances directly
from app.models.symptom import Symptom 
from app.models.problem import Problem
from app.models.question import Question 

def populate_problems_from_csv(file_path):
    """
    Populate the problems table in the database with data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing question data.
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                
                symptom_id = row['symptom_id']
                question_id = row['question_id']
                
                # Ensure that the symptom_id exists in the Symptom table
                symptom = db.session.query(Symptom).get(symptom_id)
                # Ensure that the question_id exists in the Question table
                question = db.session.query(Question).get(question_id)

                if not symptom:
                    print(f"Warning: Symptom with ID {symptom_id} not found. Skipping problem.")
                    continue

                # If question_id is not '0', ensure it exists in the Question table
                if question_id != '0':  # Treat '0' as no associated question
                    question = db.session.query(Question).get(question_id)
                    if not question:
                        print(f"Warning: Question with ID {question_id} not found. Skipping problem.")
                        question_id = None  # Set to None if invalid question_id
                else:
                    question_id = None  # No question associated, so set to None

                problem = Problem(
                    problem_id = int(row['problem_id']),
                    problem_description=row['problem_description'],
                    solution=row['solution'],

                    symptom_id=symptom_id,  # This associates the problem with a symptom
                    question_id=question_id
                )

                db.session.add(problem)

            db.session.commit()
            print("Problems table populated successfully.")

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = create_app()
    # Push application context
    with app.app_context():
        file_path = os.path.join(os.path.dirname(__file__),'../data/problems.csv')
        populate_problems_from_csv(file_path)
