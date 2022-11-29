import flask
import flask_login as flog

from . import funcs


auth = flask.Blueprint("auth", __name__)


@auth.route("/registration", methods=["GET", "POST"])
def sign_up_user() -> str | flask.Response:
    """
    GET: getting the page for registration
    POST: user registration
    """
    return funcs.sign_up_user()


@auth.route("/login", methods=["GET", "POST"])
def log_in_user() -> str | flask.Response:
    """
    GET: getting the page for login
    POST: user login
    """
    return funcs.log_in_user()


@auth.route("/logout")
@flog.login_required
def log_out_user() -> flask.Response:
    """For user logout"""
    return funcs.log_out_user()


@auth.route("/login-admin", methods=["GET", "POST"])
@flog.login_required
def log_in_admin() -> str | flask.Response:
    """
    GET: getting the page for admin login
    POST: admin login
    """
    return funcs.log_in_admin()
