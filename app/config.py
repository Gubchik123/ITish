import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


class _BaseConfig:
    """General configs"""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    DEVELOPMENT = False
    UPLOAD_FOLDER = "static"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ForProduction(_BaseConfig):
    """Production configs"""

    ENV = "production"
    SECRET_KEY = str(os.getenv("SECRET_KEY"))
    SQLALCHEMY_DATABASE_URI = str(os.getenv("DATABASE_PRODUCTION_URI"))


class ForDevelopment(_BaseConfig):
    """Development configs"""

    DEBUG = True
    DEVELOPMENT = True
    ENV = "development"
    SECRET_KEY = "secret_for_development_environment"
    SQLALCHEMY_DATABASE_URI = str(os.getenv("DATABASE_DEVELOPMENT_URI"))


class ForTesting(_BaseConfig):
    """Testing configs"""

    TESTING = True
    ENV = "testing"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "secret_for_test_environment"
    SQLALCHEMY_DATABASE_URI = str(os.getenv("DATABASE_TEST_URI"))
