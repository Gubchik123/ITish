import os

from .general import *
from .general import _get_striped_


def _check_admin_password(form, field):
    if os.getenv("ADMIN_PASSWORD") != _get_striped_(field.data):
        raise ValidationError("Wrong admin password!")


class LoginAdminForm(FlaskForm):
    password = wtf.PasswordField(
        "Admin password",
        validators=[required, _check_admin_password],
    )
    submit = wtf.SubmitField("Log In")
