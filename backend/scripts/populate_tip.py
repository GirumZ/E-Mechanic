import csv
import os
from app import create_app
from app.extensions import db
from app.models.tip import Tip

def populate_tips_from_csv(file_path):
    """
    Populate the tips table in the database with data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing tip data.
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:

                tip = Tip(
                    tip_id = int(row['tip_id']),
                    tip_short=row['tip_short'],
                    tip_long=row['tip_long']
                )
                db.session.add(tip)

            db.session.commit()
            print("Tips table populated successfully.")

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = create_app()
    # Push application context
    with app.app_context():
        file_path = os.path.join(os.path.dirname(__file__), "../data/tips.csv")
        populate_tips_from_csv(file_path)