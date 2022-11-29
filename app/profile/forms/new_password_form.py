from .general import *


class NewPasswordForm(FlaskForm):
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
        return "password"
