import os

import wtforms as wtf
from flask_wtf import FlaskForm
from wtforms import ValidationError
import wtforms.validators as validator
from werkzeug.security import check_password_hash

from ..models import User

required = validator.InputRequired("The area must be filled!")


def _get_striped_(string: str) -> str:
    return str(string).strip()


def _check_registration_username(form, field):
    if User.query.filter(User.username == _get_striped_(field.data)).first():
        raise ValidationError("There is the user with such username!")


def _check_registration_email(form, field):
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
            _check_registration_username,
        ],
    )
    email = wtf.EmailField(
        "Email",
        validators=[
            required,
            validator.Email("Enter the correct email!"),
            validator.Length(min=10, max=255),
            _check_registration_email,
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


def _check_user_email(form, field):
    if not User.query.filter(User.email == _get_striped_(field.data)).first():
        raise ValidationError("There is not the user with such email!")


def _check_user_password(form, field):
    user = User.query.filter(User.email == _get_striped_(form.email.data)).first()

    if user and not check_password_hash(user.password, _get_striped_(field.data)):
        raise ValidationError("Wrong password!")


class LoginForm(FlaskForm):
    email = wtf.EmailField(
        "Email",
        validators=[
            required,
            validator.Email("Enter the correct email!"),
            validator.Length(min=10, max=255),
            _check_user_email,
        ],
    )
    password = wtf.PasswordField(
        "Password",
        validators=[required, validator.Length(min=5), _check_user_password],
    )
    remember = wtf.BooleanField("Remember me")
    submit = wtf.SubmitField("Log In")


def _check_admin_password(form, field):
    if os.getenv("ADMIN_PASSWORD") != _get_striped_(field.data):
        raise ValidationError("Wrong admin password!")


class LoginAdminForm(FlaskForm):
    password = wtf.PasswordField(
        "Admin password",
        validators=[required, _check_admin_password],
    )
    submit = wtf.SubmitField("Log In")
