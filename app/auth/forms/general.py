import wtforms
from flask_wtf import FlaskForm
import wtforms.validators as validator

from ..services import User

required = validator.InputRequired("The area must be filled!")


def _get_striped_(string: str) -> str:
    return str(string).strip()


def _there_is_user_with_such_email(email: str) -> bool:
    return bool(User.query.filter(User.email == email).first())
