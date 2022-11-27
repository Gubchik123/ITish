import flask
import flask_login as flog

from ..models import User

from . import services
from .forms import RegistrationForm, LoginAdminForm, LoginForm


def check_if_user_is_already_authenticated(func):
    def inner():
        return (
            flask.redirect(flask.url_for("profile.get_main_page"))
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
        return flask.redirect(flask.url_for(".log_in_user"))

    return flask.render_template("auth/registration.html", form=form)


@check_if_user_is_already_authenticated
def log_in_user():
    form = LoginForm()

    if form.validate_on_submit():
        flog.login_user(
            User.query.filter(User.email == form.email.data).first(),
            remember=form.remember.data,
        )

        flask.flash("You have successfully logged in!", category="success")
        return flask.redirect(
            flask.request.args.get("next") or flask.url_for("get_home_page")
        )

    return flask.render_template("auth/login.html", form=form)


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
        return flask.redirect("/admin")

    return flask.render_template("auth/login_admin.html", form=form)
