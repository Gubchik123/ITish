import os
import flask
import flask_login as flog
from werkzeug.security import generate_password_hash

from ..models import User
from ..extensions import db
from .forms import RegistrationForm, LoginAdminForm, LoginForm


def _get_striped_(string: str) -> str:
    return str(string).strip()


def _add_user_with_data_from_(form: RegistrationForm):
    db.session.add(
        User(
            email=_get_striped_(form.email.data),
            username=_get_striped_(form.username.data),
            password=generate_password_hash(_get_striped_(form.password.data)),
        )
    )
    db.session.commit()

    flask.flash("You have successfully registered!", category="success")
    return flask.redirect(flask.url_for(".log_in_user"))


def sign_up_user():
    form = RegistrationForm()

    if flog.current_user.is_authenticated:
        return flask.redirect(flask.url_for("profile.get_main_page"))

    if form.validate_on_submit():
        return _add_user_with_data_from_(form)

    return flask.render_template("auth/registration.html", form=form)


def log_in_user():
    form = LoginForm()

    if flog.current_user.is_authenticated:
        return flask.redirect(flask.url_for("profile.get_main_page"))

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

    flask.flash("You have successfully logged out!", category="success")
    return flask.redirect(
        flask.request.args.get("next") or flask.url_for("get_home_page")
    )


def log_in_admin():
    form = LoginAdminForm()

    if form.validate_on_submit():
        flask.session["admin_logged"] = True

        return flask.redirect(flask.url_for("/admin"))

    return flask.render_template("auth/login_admin.html", form=form)
