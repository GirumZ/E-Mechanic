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

app.register_blueprint(symptom_bp)

@app.route('/')
def home():
    return "E-Mechanic is running"

if __name__ == '__main__':
    app.run(debug=True)
