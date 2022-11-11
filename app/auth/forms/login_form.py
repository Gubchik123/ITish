from werkzeug.security import check_password_hash

from .general import *
from .general import _get_striped_


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
