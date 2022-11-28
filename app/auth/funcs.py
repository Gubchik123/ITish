import flask
import flask_login as flog
from werkzeug.routing.exceptions import RoutingException

from ..exceptions import catch_flask_error_
from ..funcs import render_template, redirect_to_url_for_

from . import services
from .forms import RegistrationForm, LoginAdminForm, LoginForm


@catch_flask_error_(RoutingException)
def _get_url_for_user_profile_page():
    return flask.url_for("profile.get_user_with_", username=flog.current_user.username)


def check_if_user_is_already_authenticated(func):
    def inner():
        return (
            flask.redirect(_get_url_for_user_profile_page())
            if flog.current_user.is_authenticated
            else func()
        )

    return inner


@check_if_user_is_already_authenticated
def sign_up_user():
    form = RegistrationForm()

    if form.validate_on_submit():
        services._add_user_in_db_with_data_from_(form)

        flask.flash("You have successfully registered!", category="success")
        return redirect_to_url_for_(".log_in_user")

    return render_template("auth/registration.html", form=form)


@check_if_user_is_already_authenticated
@catch_flask_error_(RoutingException)
def log_in_user():
    form = LoginForm()

    if form.validate_on_submit():
        services._log_in_user_with_data_from_(form)

        flask.flash("You have successfully logged in!", category="success")
        return flask.redirect(
            flask.request.args.get("next") or _get_url_for_user_profile_page()
        )

    return render_template("auth/login.html", form=form)


@catch_flask_error_(RoutingException)
def log_out_user():
    flog.logout_user()
    flask.session["admin_logged"] = False

    flask.flash("You have successfully logged out!", category="success")
    return flask.redirect(
        flask.request.args.get("next") or flask.url_for("get_home_page")
    )


def log_in_admin():
    form = LoginAdminForm()

    if form.validate_on_submit():
        flask.session["admin_logged"] = True
        return redirect_to_url_for_("admin.index")

    return render_template("auth/login_admin.html", form=form)
