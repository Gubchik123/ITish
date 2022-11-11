from .general import *
from .general import _get_striped_


def _check_username(form, field):
    if User.query.filter(User.username == _get_striped_(field.data)).first():
        raise ValidationError("There is the user with such username!")


def _check_email(form, field):
    if User.query.filter(User.email == _get_striped_(field.data)).first():
        raise ValidationError("There is the user with such email!")


class RegistrationForm(FlaskForm):
    username = wtf.StringField(
        "Username",
        validators=[
            required,
            validator.Length(min=3, max=50),
            validator.Regexp(
                # (no _ or . at the beginning)[allowed allowed characters](no _ or . at the end)
                r"^(?![_.])[a-zA-Z0-9._]+(?<![_.])$",
                message="Wrong username (must be neither spaces nor _ or . at the beginning and at the end)!",
            ),
            _check_username,
        ],
    )
    email = wtf.EmailField(
        "Email",
        validators=[
            required,
            validator.Email("Enter the correct email!"),
            validator.Length(min=10, max=255),
            _check_email,
        ],
    )
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
    submit = wtf.SubmitField("Sign Up")
