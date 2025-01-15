from app import db
class Symptom(db.Model):
    __tablename__ = 'symptoms'

    id = db.Column(db.Integer, primary_key=True)
    symptom_text = db.Column(db.String(255), nullable=False)
    sensation = db.Column(db.String(255), nullable=True)
    followup_available = db.Column(db.Boolean, nullable=False)

    # Relationship with Question
    questions = db.relationship('Question', backref='symptom', lazy=True)

    def __repr__(self):
        return f"<Symptom {self.symptom_text}>"


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'), nullable=False)

    # Relationship with Problem
    problems = db.relationship('Problem', backref='question', lazy=True)

    def __repr__(self):
        return f"<Question {self.question_text}>"


class Problem(db.Model):
    __tablename__ = 'problems'

    id = db.Column(db.Integer, primary_key=True)
    problem_description = db.Column(db.String(255), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)

    def __repr__(self):
        return f"<Problem {self.problem_description}>"


class Tip(db.Model):
    __tablename__ = 'tips'

    id = db.Column(db.Integer, primary_key=True)
    tip_description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Tip {self.tip_description}>"


class OBDCode(db.Model):
    __tablename__ = 'obd'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<OBDCode {self.code}>"
