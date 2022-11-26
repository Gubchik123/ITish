from typing import NamedTuple

import flask
import flask_login as flog
from sqlalchemy import desc
from werkzeug.security import generate_password_hash

from ..app import app
from ..models import User
from ..extensions import db
from .forms import UserAvatarForm, NewEmailForm, NewUsernameForm, NewPasswordForm


class Forms(NamedTuple):
    new_email_form: NewEmailForm
    new_username_form: NewUsernameForm
    new_password_form: NewPasswordForm


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

    return flask.redirect(
        flask.url_for("profile.get_user_with_", username=flog.current_user.username)
    )


@_check_if_it_is_current_user
def delete_user(username: str):
    pass


@_check_if_it_is_current_user
def get_edit_page(username: str):
    return flask.render_template(
        "profile/edit.html",
        forms=(NewEmailForm(), NewUsernameForm(), NewPasswordForm()),
    )


def _check_if_info_validate_on_submit_in_(
    form: NewEmailForm | NewUsernameForm | NewPasswordForm,
):
    def decorator(func):
        @_check_if_it_is_current_user
        def inner(username: str):
            if form().validate_on_submit():
                func(username)
                return flask.redirect(
                    flask.url_for(
                        "profile.get_user_with_", username=flog.current_user.username
                    )
                )

            flask.flash("Error! You entered wrong data!", category="danger")

            return flask.redirect(
                flask.url_for(
                    "profile.get_edit_page", username=flog.current_user.username
                )
            )

        return inner

    return decorator


@_check_if_info_validate_on_submit_in_(NewEmailForm)
def edit_email(username: str):
    flog.current_user.email = NewEmailForm().email.data
    db.session.commit()
    flask.flash("Email has successfully changed", category="success")


@_check_if_info_validate_on_submit_in_(NewUsernameForm)
def edit_username(username: str):
    flog.current_user.username = NewUsernameForm().username.data
    db.session.commit()
    flask.flash("Username has successfully changed", category="success")


@_check_if_info_validate_on_submit_in_(NewPasswordForm)
def edit_password(username: str):
    flog.current_user.password = generate_password_hash(NewPasswordForm().password.data)
    db.session.commit()
    flask.flash("Password has successfully changed", category="success")
