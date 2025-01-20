from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

from routes.symptom_routes import symptom_bp
from routes.question_routes import question_bp
from routes.problem_routes import problem_bp
from routes.tip_routes import tip_pb
from routes.obd_routes import obd_bp

app.register_blueprint(symptom_bp)
app.register_blueprint(question_bp)
app.register_blueprint(problem_bp)
app.register_blueprint(tip_pb)
app.register_blueprint(obd_bp)

@app.route('/')
def home():
    return "E-Mechanic is running"

if __name__ == '__main__':
    app.run(debug=True)
