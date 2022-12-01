import flask
import flask_login as flog

from ..funcs import render_template, redirect_to_url_for_

from . import services
from .forms import RegistrationForm, LoginAdminForm, LoginForm


def _redirect_to_user_profile_page() -> flask.Response:
    """For getting url for the profile page for current user"""
    return redirect_to_url_for_(
        "profile.get_user_with_", username=flog.current_user.username
    )


def check_if_user_is_already_authenticated(func):
    """The decorator for checking if user is authenticated"""

    def inner():
        return (
            _redirect_to_user_profile_page()
            if flog.current_user.is_authenticated
            else func()
        )

    return inner


@check_if_user_is_already_authenticated
def sign_up_user() -> str | flask.Response:
    """
    GET: rendering template for the page for registration
    POST: user registration and redirecting to the page for login
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        services._add_user_in_db_with_data_from_(form)

        flask.flash("You have successfully registered!", category="success")
        return redirect_to_url_for_(".log_in_user")

    return render_template("auth/registration.html", form=form)


@check_if_user_is_already_authenticated
def log_in_user() -> str | flask.Response:
    """
    GET: rendering template for the page for user login
    POST: user login and redirecting to next url or user profile page
    """
    form = LoginForm()

    if form.validate_on_submit():
        services._log_in_user_with_data_from_(form)

        flask.flash("You have successfully logged in!", category="success")
        next_url = flask.request.args.get("next")
        return (
            flask.redirect(next_url) if next_url else _redirect_to_user_profile_page()
        )

    return render_template("auth/login.html", form=form)


def log_out_user() -> flask.Response:
    """For user logout and redirecting to next url or 'Home' page"""
    flog.logout_user()
    flask.session["admin_logged"] = False

    flask.flash("You have successfully logged out!", category="success")
    next_url = flask.request.args.get("next")
    return (
        flask.redirect(next_url) if next_url else redirect_to_url_for_("get_home_page")
    )


def log_in_admin() -> str | flask.Response:
    """
    GET: rendering template for the page for admin login
    POST: admin login and redirecting to the admin panel
    """
    form = LoginAdminForm()

    if form.validate_on_submit():
        flask.session["admin_logged"] = True
        return redirect_to_url_for_("admin.index")

    return render_template("auth/login_admin.html", form=form)
