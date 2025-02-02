import csv
import os
from app import create_app
from app.extensions import db
from app.models.symptom import Symptom  # Import your Symptom model

def populate_symptoms_from_csv(file_path):
    """
    Populate the symptoms table in the database with data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing symptom data.
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert followup_available to boolean if needed
                followup_available = row['followup_available'].strip().lower() in ['true', '1', 'yes']

                symptom = Symptom(
                    symptom_id = int(row['symptom_id']),
                    symptom_text=row['symptom_text'],
                    sensation=row.get('sensation'),
                    followup_available=followup_available
                )

                db.session.add(symptom)

            db.session.commit()
            print("Symptoms table populated successfully.")

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = create_app()
    # Push application context
    with app.app_context():
        file_path = os.path.join(os.path.dirname(__file__), "../data/symptoms.csv")
        populate_symptoms_from_csv(file_path)
