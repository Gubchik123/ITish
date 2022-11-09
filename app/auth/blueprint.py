import flask_login as flog
from flask import Blueprint

from . import funcs


auth = Blueprint("auth", __name__)


@auth.route("/registration", methods=["GET", "POST"])
def sign_up_user():
    return funcs.sign_up_user()


@auth.route("/login", methods=["GET", "POST"])
def log_in_user():
    return funcs.log_in_user()


@auth.route("/logout", methods=["GET", "POST"])
@flog.login_required
def log_out_user():
    return funcs.log_out_user()


@auth.route("/login-admin", methods=["GET", "POST"])
def log_in_admin():
    return funcs.log_in_admin()
