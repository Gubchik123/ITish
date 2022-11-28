import flask_login as flog
from werkzeug.security import generate_password_hash

from ..models import User
from ..extensions import db
from ..exceptions import catch_sqlalchemy_errors

from .forms import RegistrationForm, LoginForm


def _get_striped_(string: str) -> str:
    return str(string).strip()


@catch_sqlalchemy_errors
def _add_user_in_db_with_data_from_(form: RegistrationForm):
    db.session.add(
        User(
            email=_get_striped_(form.email.data),
            username=_get_striped_(form.username.data),
            password=generate_password_hash(_get_striped_(form.password.data)),
        )
    )
    db.session.commit()


@catch_sqlalchemy_errors
def _log_in_user_with_data_from_(form: LoginForm):
    flog.login_user(
        User.query.filter(User.email == form.email.data).first(),
        remember=form.remember.data,
    )
