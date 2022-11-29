from .general import *
from .general import _get_striped_, _there_is_user_with_such_email


def _there_is_user_with_such_username(username: str) -> bool:
    """For checking on exist user with such username"""
    return bool(User.query.filter(User.username == username).first())


def _check_username(form, field: wtforms.StringField) -> None:
    """For checking user username from username field data"""
    if _there_is_user_with_such_username(_get_striped_(field.data)):
        raise wtforms.ValidationError("There is the user with such username!")


def _check_email(form, field: wtforms.EmailField) -> None:
    """For checking on exist user with such email"""
    if _there_is_user_with_such_email(_get_striped_(field.data)):
        raise wtforms.ValidationError("There is the user with such email!")


class RegistrationForm(FlaskForm):
    """Form for user registration with username, email and password"""

    username = wtforms.StringField(
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
    email = wtforms.EmailField(
        "Email",
        validators=[
            required,
            validator.Email("Enter the correct email!"),
            validator.Length(min=10, max=255),
            _check_email,
        ],
    )
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
    submit = wtforms.SubmitField("Sign Up")
