import os
from dotenv import load_dotenv


load_dotenv()


class _BaseConfig:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    DEVELOPMENT = False
    UPLOAD_FOLDER = "static"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = str(os.getenv("DATABASE_URI"))


class ForProduction(_BaseConfig):
    ENV = "production"
    SECRET_KEY = str(os.getenv("SECRET_KEY"))


class ForDevelopment(_BaseConfig):
    DEBUG = True
    DEVELOPMENT = True
    ENV = "development"
    SECRET_KEY = "secret_for_development_environment"


class ForTesting(_BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "secret_for_test_environment"
