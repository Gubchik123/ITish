import wtforms
from flask_wtf import FlaskForm
import wtforms.validators as validator

from ..services import User

required = validator.InputRequired("The area must be filled!")


def _there_is_user_with_such_email(email: str) -> bool:
    """For checking on exist user in database"""
    return bool(User.query.filter(User.email == email).first())


def _get_striped_(string: str) -> str:
    """For getting striped string

    Args:
        string (str): some string for striping

    Returns:
        str: striped string
    """
    return str(string).strip()
