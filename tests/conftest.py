import pytest
from werkzeug.security import generate_password_hash

from app.app import app
from app.models import User, Post, Tag, Like, Comment


@pytest.fixture(scope="module")
def test_app():
    """Fixture for getting the Flask testing application"""
    app.config.from_object("app.config.ForTesting")

    with app.app_context():
        yield app  # Testing happens here


@pytest.fixture(scope="module")
def test_client():
    """Fixture for getting test client of the Flask application"""

    # Create a test client using the Flask application
    with app.test_client() as testing_client:
        yield testing_client


@pytest.fixture(scope="module")
def new_user():
    """Fixture for getting new user for testing"""
    return User(
        username="test_username",
        email="test_email@gmail.com",
        password=generate_password_hash("test_password"),
    )


@pytest.fixture(scope="module")
def new_post():
    """Fixture for getting new post for testing"""
    return Post(title="Test title", body="<h2>Test post content</h2>", user_id=1)


@pytest.fixture(scope="module")
def new_tag():
    """Fixture for getting new tag for testing"""
    return Tag(title="test tag")


@pytest.fixture(scope="module")
def new_like():
    """Fixture for getting new like for testing"""
    return Like(user_id=1, post_id=1)


@pytest.fixture(scope="module")
def new_comment():
    """Fixture for getting new comment for testing"""
    return Comment(body="Test comment", user_id=1, post_id=1)
