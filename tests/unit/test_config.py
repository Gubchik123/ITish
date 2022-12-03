import os


def test_development_config(test_app):
    """
    GIVEN the Flask testing application
    WHEN the development config is setting
    THEN check the config of the development application
    """
    test_app.config.from_object("app.config.ForDevelopment")

    assert test_app.config["DEBUG"] == True
    assert test_app.config["TESTING"] == False
    assert test_app.config["ENV"] == "development"
    assert test_app.config["DEVELOPMENT"] == True
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == str(
        os.getenv("DATABASE_DEVELOPMENT_URI")
    )
    assert test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] == False
    assert test_app.config["SECRET_KEY"] == "secret_for_development_environment"


def test_production_config(test_app):
    """
    GIVEN the Flask testing application
    WHEN the production config is setting
    THEN check the config of the production application
    """
    test_app.config.from_object("app.config.ForProduction")

    assert test_app.config["DEBUG"] == False
    assert test_app.config["TESTING"] == False
    assert test_app.config["ENV"] == "production"
    assert test_app.config["DEVELOPMENT"] == False
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == str(
        os.getenv("DATABASE_PRODUCTION_URI")
    )
    assert test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] == False
    assert test_app.config["SECRET_KEY"] == str(os.getenv("SECRET_KEY"))


def test_testing_config(test_app):
    """
    GIVEN the Flask testing application
    WHEN the testing config is setting
    THEN check the config of the testing application
    """
    test_app.config.from_object("app.config.ForTesting")

    assert test_app.config["DEBUG"] == False
    assert test_app.config["TESTING"] == True
    assert test_app.config["ENV"] == "testing"
    assert test_app.config["DEVELOPMENT"] == False
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == str(
        os.getenv("DATABASE_TEST_URI")
    )
    assert test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] == True
    assert test_app.config["SECRET_KEY"] == "secret_for_test_environment"
