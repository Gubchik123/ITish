import os
from dotenv import load_dotenv


load_dotenv()


class _Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    UPLOAD_FOLDER = "static"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")


class ForProduction(_Config):
    ENV = "production"
    SECRET_KEY = os.getenv("SECRET_KEY")


class ForDevelopment(_Config):
    DEBUG = True
    DEVELOPMENT = True
    ENV = "development"
    SECRET_KEY = "secret_for_development_environment"


class ForTesting(_Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "secret_for_test_environment"
