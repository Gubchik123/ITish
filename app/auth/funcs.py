import flask
from werkzeug.security import generate_password_hash

from ..models import User
from ..extensions import db
from .forms import RegistrationForm, LoginAdminForm, LoginForm


def _get_striped_(string: str) -> str:
    return string.strip()


def _check_user_with_data_from_(form: RegistrationForm):
    if User.query.filter(User.email == _get_striped_(form.email.data)).first():
        flask.flash("There is the user with such email!", category="danger")
        return False

    if User.query.filter(User.username == _get_striped_(form.username.data)).first():
        flask.flash("There is the user with such username!", category="danger")
        return False

    return True


def _add_user_with_data_from_(form: RegistrationForm):
    db.session.add(
        User(
            email=_get_striped_(form.email.data),
            username=_get_striped_(form.username.data),
            password=generate_password_hash(_get_striped_(form.username.data)),
        )
    )
    db.session.commit()

    flask.flash("You have successfully registered!", category="success")
    return flask.redirect(flask.url_for(".log_in_user"))


def sign_up_user():
    form = RegistrationForm()

    if form.validate_on_submit() and _check_user_with_data_from_(form):
        return _add_user_with_data_from_(form)

    return flask.render_template("auth/registration.html", form=form)


def log_in_user():
    form = LoginForm()
    return flask.render_template("auth/login.html")


def log_out_user():
    pass


def log_in_admin():
    form = LoginAdminForm()
    return flask.render_template("auth/login_admin.html")
