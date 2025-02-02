from app.extensions import db

class Question(db.Model):
    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.symptom_id'), nullable=False)

    # Relationship with Problem
    problems = db.relationship('Problem', backref='question', lazy=True)

    def __repr__(self):
        return f"<Question {self.question_text}>"