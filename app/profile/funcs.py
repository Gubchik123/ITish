import flask
import flask_login as flog

from ..app import app
from ..models import User
from ..funcs import render_template, redirect_to_url_for_

from . import services
from .forms import UserAvatarForm, NewEmailForm, NewUsernameForm, NewPasswordForm


def _check_if_it_is_current_user(func):
    """The decorator for checking if current user get page"""

    def inner(username: str):
        return (
            flask.abort(403)
            if flog.current_user.username != username
            else func(username)
        )

    return inner


def get_user_with_(username: str) -> str:
    """For rendering the profile page for user by username"""
    allowed_tabs = ["", "overview", "posts", "comments", "likes"]

    if flask.request.args.get("tab", "") not in allowed_tabs:
        return flask.abort(404)

    return render_template(
        "profile/index.html",
        form=UserAvatarForm(),
        user=User.query.filter(User.username == username).first_or_404(),
    )


def get_avatar_for_user_with_(username: str) -> flask.Response:
    """For getting avatar from database for user by username"""
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


def _redirect_on_current_user_profile_page() -> flask.Response:
    """For redirecting to the profile page by current user username"""
    return redirect_to_url_for_(
        "profile.get_user_with_", username=flog.current_user.username
    )


@_check_if_it_is_current_user
def update_user_avatar(username: str) -> flask.Response:
    """For validating user avatar form and redirecting to the profile page"""
    if UserAvatarForm().validate_on_submit():
        services._update_current_user_avatar_in_db()
        flask.flash("Avatar has successfully updated", category="success")
    else:
        flask.flash("Error! Wrong file type for avatar image", category="danger")

    return _redirect_on_current_user_profile_page()


@_check_if_it_is_current_user
def delete_current_user(username: str) -> flask.Response:
    """For deleting current user from db and redirecting to the 'Home' page"""
    services._delete_current_user_from_db()

    flask.flash("Profile has successfully deleted", category="success")
    return redirect_to_url_for_("get_home_page")


@_check_if_it_is_current_user
def get_edit_page(username: str) -> str:
    """For rendering the template for the page for editing user information"""
    return render_template(
        "profile/edit.html",
        forms=(NewEmailForm(), NewUsernameForm(), NewPasswordForm()),
    )


def _check_if_info_validate_on_submit_in_(
    form: NewEmailForm | NewUsernameForm | NewPasswordForm,
) -> flask.Response:
    """
    The decorator for checking if form is validate on submit before editing

    If form is validate redirect to the current user profile page
    else redirect to the page for user editing with flashed message
    """

    def decorator(func):
        @_check_if_it_is_current_user
        def inner(username: str) -> flask.Response:
            if form().validate_on_submit():
                func(username)
                return _redirect_on_current_user_profile_page()

            flask.flash("Error! You entered wrong data!", category="danger")

            return redirect_to_url_for_(
                "profile.get_edit_page", username=flog.current_user.username
            )

        return inner

    return decorator


@_check_if_info_validate_on_submit_in_(NewEmailForm)
def edit_current_user_email(username: str) -> flask.Response:
    """For editing user username if new username form is validate"""
    services._edit_current_user_email_in_db()
    flask.flash("Email has successfully changed", category="success")


@_check_if_info_validate_on_submit_in_(NewUsernameForm)
def edit_current_user_username(username: str) -> flask.Response:
    """For editing user email if new email form is validate"""
    services._edit_current_user_username_in_db()
    flask.flash("Username has successfully changed", category="success")


@_check_if_info_validate_on_submit_in_(NewPasswordForm)
def edit_current_user_password(username: str) -> flask.Response:
    """For editing user password if new password form is validate"""
    services._edit_current_user_password_in_db()
    flask.flash("Password has successfully changed", category="success")
