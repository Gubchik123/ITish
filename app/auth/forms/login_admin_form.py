import os

from .general import *
from .general import _get_striped_


def _check_admin_password(form, field: wtforms.PasswordField) -> None:
    """For checking admin password from password field data"""
    if str(os.getenv("ADMIN_PASSWORD")) != _get_striped_(field.data):
        raise wtforms.ValidationError("Wrong admin password!")


class LoginAdminForm(FlaskForm):
    """Form for admin login by admin password"""

    password = wtforms.PasswordField(
        "Admin password",
        validators=[required, _check_admin_password],
    )
    submit = wtforms.SubmitField("Log In")
