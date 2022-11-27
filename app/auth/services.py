from werkzeug.security import generate_password_hash

from ..models import User
from ..extensions import db
from .forms import RegistrationForm


def _get_striped_(string: str) -> str:
    return str(string).strip()


def _add_user_in_db_with_data_from_(form: RegistrationForm):
    db.session.add(
        User(
            email=_get_striped_(form.email.data),
            username=_get_striped_(form.username.data),
            password=generate_password_hash(_get_striped_(form.password.data)),
        )
    )
    db.session.commit()
