import flask

from . import funcs
from .app import app

from .auth.blueprint import auth
from .blog.blueprint import blog
from .profile.blueprint import profile


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(blog, url_prefix="/blog")
app.register_blueprint(profile, url_prefix="/user")


@app.route("/")
def get_home_page() -> str:
    """For getting the 'Home' page"""
    return funcs.get_home_page()


@app.route("/FAQs")
def get_FAQs_page() -> str:
    """For getting the 'FAQs' page"""
    return funcs.get_FAQs_page()


@app.route("/feedback")
def get_feedback_page() -> str:
    """For getting the 'Feedback' page"""
    return funcs.get_feedback_page()


@app.errorhandler(401)
def redirect_to_login_page(error) -> flask.Response:
    """For handling error code 401"""
    return funcs.redirect_to_login_page()


@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(501)
def get_error_page(error) -> tuple[str, int]:
    """For handling some HTTP error codes"""
    return funcs.get_error_page(error)
