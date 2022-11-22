import flask_login as flog
from flask import Blueprint

from . import funcs


profile = Blueprint("profile", __name__)


@profile.route("/get-user-avatar")
@flog.login_required
def get_user_avatar():
    return funcs.get_user_avatar()


@profile.route("/update-user-avatar", methods=["POST"])
def update_user_avatar():
    return funcs.update_user_avatar()


@profile.route("/<username>")
def get_user_with_(username: str):
    return funcs.get_user_with_(username)


@profile.route("/<username>/delete")
@flog.login_required
def delete_user_with_(username: str):
    return funcs.delete_user_with_(username)


@profile.route("/<username>/edit", methods=["GET", "POST"])
@flog.login_required
def edit_user_with_(username: str):
    return funcs.edit_user_with_(username)
