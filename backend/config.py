from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/e_mechanic')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
