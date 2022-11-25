import flask
import flask_login as flog
from sqlalchemy import desc

from ..app import app
from ..models import User
from ..extensions import db
from .forms import UserAvatarForm


def _check_if_it_is_current_user(func):
    def inner(username: str):
        return (
            flask.abort(403)
            if flog.current_user.username != username
            else func(username)
        )

    return inner


def get_user_with_(username: str):
    form = UserAvatarForm()
    tabs = ["", "overview", "posts", "comments", "likes"]

    if flask.request.args.get("tab", "") not in tabs:
        return flask.abort(404)

    return flask.render_template(
        "profile/index.html",
        form=form,
        user=User.query.filter(User.username == username).first_or_404(),
    )


def get_avatar_for_user_with_(username: str):
    user_avatar = User.query.filter(User.username == username).first().avatar

    if user_avatar:
        response = flask.make_response(user_avatar)
    else:
        path_to_default_avatar = app.root_path + flask.url_for(
            "static", filename="images/default_ava.png"
        )
        with open(path_to_default_avatar, "rb") as file:
            response = flask.make_response(file.read())

    response.headers["Content-Type"] = "image/png"
    return response


@_check_if_it_is_current_user
def update_user_avatar(username: str):
    if UserAvatarForm().validate_on_submit():
        avatar_image = flask.request.files["avatar_image"]

        flog.current_user.avatar = avatar_image.read()
        db.session.commit()

        flask.flash("Avatar has successfully updated", category="success")
    else:
        flask.flash("Error. Wrong file type for avatar image", category="danger")

    return flask.redirect(flask.url_for("profile.get_user_with_", username=username))


@_check_if_it_is_current_user
def delete_user_with_(username: str):
    pass


@_check_if_it_is_current_user
def edit_user_with_(username: str):
    pass
