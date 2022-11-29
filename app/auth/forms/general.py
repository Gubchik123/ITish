import wtforms
from flask_wtf import FlaskForm
import wtforms.validators as validator

from ..services import User, _get_striped_

required = validator.InputRequired("The area must be filled!")


def _there_is_user_with_such_email(email: str) -> bool:
    """For checking on exist user in database"""
    return bool(User.query.filter(User.email == email).first())
