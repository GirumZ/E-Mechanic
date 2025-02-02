from flask import Flask
from config import Config
from app.extensions import db, cors, migrate



def create_app():
    app = Flask(__name__)
    cors.init_app(app)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.symptom_routes import symptom_bp
    from app.routes.question_routes import question_bp
    from app.routes.problem_routes import problem_bp
    from app.routes.tip_routes import tip_pb
    from app.routes.obd_routes import obd_bp

    app.register_blueprint(symptom_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(problem_bp)
    app.register_blueprint(tip_pb)
    app.register_blueprint(obd_bp)

    return app