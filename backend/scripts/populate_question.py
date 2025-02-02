import csv
import os
from app import create_app
from app.extensions import db
from app.models.question import Question 
from app.models.symptom import Symptom

def populate_questions_from_csv(file_path):
    """
    Populate the questions table in the database with data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing question data.
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Get the symptom_id and ensure it exists in the database
                symptom_id = row['symptom_id']
                
                # Ensure that the symptom_id exists in the Symptom table
                symptom = db.session.query(Symptom).get(symptom_id)
                if not symptom:
                    print(f"Warning: Symptom with ID {symptom_id} not found. Skipping question.")
                    continue

                question = Question(
                    question_text=row['question_text'],
                    symptom_id=symptom_id  # This associates the question with a symptom
                )

                db.session.add(question)

            db.session.commit()
            print("Questions table populated successfully.")

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = create_app()
    # Push application context
    with app.app_context():
        file_path = os.path.join(os.path.dirname(__file__), "../data/questions.csv")
        populate_questions_from_csv(file_path)
