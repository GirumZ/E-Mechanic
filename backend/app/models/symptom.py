from app.extensions import db

class Symptom(db.Model):
    __tablename__ = 'symptoms'

    symptom_id = db.Column(db.Integer, primary_key=True)
    symptom_text = db.Column(db.String(255), nullable=False)
    sensation = db.Column(db.String(255), nullable=True)
    followup_available = db.Column(db.Boolean, nullable=False)

    # Relationship with Question
    questions = db.relationship('Question', backref='symptom', lazy=True)

    def __repr__(self):
        return f"<Symptom {self.symptom_text}>"