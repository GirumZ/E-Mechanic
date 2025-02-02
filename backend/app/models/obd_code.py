from app.extensions import db

class OBDCode(db.Model):
    __tablename__ = 'obd'

    obd_id = db.Column(db.Integer, primary_key=True)
    obd_code = db.Column(db.String(50), nullable=False)
    obd_description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<OBDCode {self.obd_code}>"