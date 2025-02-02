from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Database
db = SQLAlchemy()

# Database migrations
migrate = Migrate()

# CORS (Cross-Origin Resource Sharing)
cors = CORS()