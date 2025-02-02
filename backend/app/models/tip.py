from app.extensions import db

class Tip(db.Model):
    __tablename__ = 'tips'

    tip_id = db.Column(db.Integer, primary_key=True)
    tip_short = db.Column(db.String(255), nullable=False)
    tip_long = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Tip {self.tip_short}>"