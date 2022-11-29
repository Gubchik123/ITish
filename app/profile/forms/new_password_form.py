from .general import *


class NewPasswordForm(FlaskForm):
    """Form for editing user password"""

    password = wtforms.PasswordField(
        "Password", validators=[required, validator.Length(min=5)]
    )
    password_again = wtforms.PasswordField(
        "Password again",
        validators=[
            required,
            validator.Length(min=5),
            validator.EqualTo("password", message="Passwords must match!"),
        ],
    )
    submit = wtforms.SubmitField("Change password")

    def get_string_for_action(self) -> str:
        """For getting form name for form action in the editing template"""
        return "password"
