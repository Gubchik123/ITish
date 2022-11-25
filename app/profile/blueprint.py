import flask_login as flog
from flask import Blueprint

from . import funcs


profile = Blueprint("profile", __name__)


@profile.route("/<username>")
def get_user_with_(username: str):
    return funcs.get_user_with_(username)


@profile.route("/<username>/get-user-avatar")
def get_avatar_for_user_with_(username: str):
    return funcs.get_avatar_for_user_with_(username)


@profile.route("/<username>/update-user-avatar", methods=["POST"])
def update_user_avatar(username: str):
    return funcs.update_user_avatar(username)


@profile.route("/<username>/delete")
@flog.login_required
def delete_user_with_(username: str):
    return funcs.delete_user_with_(username)


@profile.route("/<username>/edit", methods=["GET", "POST"])
@flog.login_required
def edit_user_with_(username: str):
    return funcs.edit_user_with_(username)
