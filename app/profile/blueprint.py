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
def delete_user(username: str):
    return funcs.delete_user(username)


@profile.route("/<username>/edit", methods=["GET", "POST"])
def get_edit_page(username: str):
    return funcs.get_edit_page(username)


@profile.route("/<username>/edit-email", methods=["POST"])
def edit_email(username: str):
    return funcs.edit_email(username)


@profile.route("/<username>/edit-username", methods=["POST"])
def edit_username(username: str):
    return funcs.edit_username(username)


@profile.route("/<username>/edit-password", methods=["POST"])
def edit_password(username: str):
    return funcs.edit_password(username)
