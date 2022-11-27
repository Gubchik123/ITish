from werkzeug.security import check_password_hash

from .general import *
from .general import _get_striped_
from .general import _there_is_user_with_such_email


def _check_user_email(form, field):
    if not _there_is_user_with_such_email(_get_striped_(field.data)):
        raise wtforms.ValidationError("There is not the user with such email!")


def _check_user_password(form, field):
    user = User.query.filter(User.email == _get_striped_(form.email.data)).first()

    if user and not check_password_hash(user.password, _get_striped_(field.data)):
        raise wtforms.ValidationError("Wrong password!")


class LoginForm(FlaskForm):
    email = wtforms.EmailField(
        "Email",
        validators=[
            required,
            validator.Email("Enter the correct email!"),
            validator.Length(min=10, max=255),
            _check_user_email,
        ],
    )
    password = wtforms.PasswordField(
        "Password",
        validators=[required, validator.Length(min=5), _check_user_password],
    )
    remember = wtforms.BooleanField("Remember me")
    submit = wtforms.SubmitField("Log In")
