import wtforms
from flask_wtf import FlaskForm
import wtforms.validators as validator

from ..funcs import User


required = validator.InputRequired("The area must be filled!")


def _get_striped_(string: str) -> str:
    """For getting striped string

    Args:
        string (str): some string for striping

    Returns:
        str: striped string
    """
    return str(string).strip()
