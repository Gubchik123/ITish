import flask
import flask_login as flog

from . import funcs


profile = flask.Blueprint("profile", __name__)


@profile.route("/<username>")
@flog.login_required
def get_user_with_(username: str) -> str:
    return funcs.get_user_with_(username)


@profile.route("/<username>/get-user-avatar")
def get_avatar_for_user_with_(username: str) -> flask.Response:
    return funcs.get_avatar_for_user_with_(username)


@profile.route("/<username>/update-user-avatar", methods=["POST"])
def update_user_avatar(username: str) -> flask.Response:
    return funcs.update_user_avatar(username)


@profile.route("/<username>/delete")
def delete_current_user(username: str) -> flask.Response:
    return funcs.delete_current_user(username)


@profile.route("/<username>/edit", methods=["GET", "POST"])
def get_edit_page(username: str) -> str:
    return funcs.get_edit_page(username)


@profile.route("/<username>/edit-email", methods=["POST"])
def edit_current_user_email(username: str) -> flask.Response:
    return funcs.edit_current_user_email(username)


@profile.route("/<username>/edit-username", methods=["POST"])
def edit_current_user_username(username: str) -> flask.Response:
    return funcs.edit_current_user_username(username)


@profile.route("/<username>/edit-password", methods=["POST"])
def edit_current_user_password(username: str) -> flask.Response:
    return funcs.edit_current_user_password(username)
