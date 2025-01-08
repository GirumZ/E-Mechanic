from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
# from models import db, Symptom, Question, Problem, Tip, OBDCode

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

@app.route('/')
def home():
    return "E-Mechanic is running"

if __name__ == '__main__':
    app.run(debug=True)
