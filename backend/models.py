from app import db

class BaseModel(db.Model):
    """Base class for all models to avoid repetition of the 'id' column definition."""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)



class Symptom(BaseModel):
    __tablename__ = 'symptoms'

    symptem_text = db.Column(db.String(255), nullable=False)
    sensation = db.Column(db.String(255), nullable=True)
    followup_available = db.Column(db.Boolean, nullable=False, default=False)

    # Relationship with Question
    questions = db.relationship('Question', backref='symptom', lazy=True)

    def __repr__(self):
        return f"<Symptom {self.symptem_text}>"


class Question(BaseModel):
    __tablename__ = 'questions'

    question_text = db.Column(db.String(255), nullable=False)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'), nullable=False)

    # Relationship with Problem
    problems = db.relationship('Problem', backref='question', lazy=True)

    def __repr__(self):
        return f"<Question {self.question_text}>"


class Problem(BaseModel):
    __tablename__ = 'problems'

    problem_description = db.Column(db.String(255), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)

    def __repr__(self):
        return f"<Problem {self.problem_description}>"


class Tip(BaseModel):
    __tablename__ = 'tips'

    tip_description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Tip {self.tip_description}>"


class OBDCode(BaseModel):
    __tablename__ = 'obd'

    code = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<OBDCode {self.code}>"
