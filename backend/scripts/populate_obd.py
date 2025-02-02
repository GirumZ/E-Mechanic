import os
import csv
from app import create_app
from app.extensions import db
from app.models.obd_code import OBDCode

def populate_obd_from_csv(file_path):
    """
    Populate the obd table in the database with data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing tip data.
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:

                obd = OBDCode(
                    obd_id = int(row['obd_id']),
                    obd_code=row['obd_code'],
                    obd_description=row['obd_description']
                )
                db.session.add(obd)

            db.session.commit()
            print("Obd table populated successfully.")

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create the Flask app
    app = create_app()

    # Push application context
    with app.app_context():
        file_path = os.path.join(os.path.dirname(__file__), "../data/obds.csv")
        populate_obd_from_csv(file_path)