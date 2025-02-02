from app.extensions import db

class Problem(db.Model):
    __tablename__ = 'problems'

    problem_id = db.Column(db.Integer, primary_key=True)
    problem_description = db.Column(db.String(516), nullable=False)
    solution = db.Column(db.String(516), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), nullable=True)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.symptom_id'), nullable=False)
    def __repr__(self):
        return f"<Problem {self.problem_description}>"