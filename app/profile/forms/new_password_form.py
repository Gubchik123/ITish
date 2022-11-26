from .general import *


class NewPasswordForm(FlaskForm):
    password = wtf.PasswordField(
        "Password", validators=[required, validator.Length(min=5)]
    )
    password_again = wtf.PasswordField(
        "Password again",
        validators=[
            required,
            validator.Length(min=5),
            validator.EqualTo("password", message="Passwords must match!"),
        ],
    )
    submit = wtf.SubmitField("Change password")

    def get_string_for_action(self) -> str:
        return "password"
