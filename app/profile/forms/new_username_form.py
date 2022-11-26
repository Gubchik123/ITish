from .general import *
from .general import _get_striped_


def _check_username(form, field):
    if User.query.filter(User.username == _get_striped_(field.data)).first():
        raise wtf.ValidationError("There is the user with such username!")


class NewUsernameForm(FlaskForm):
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
    submit = wtf.SubmitField("Change username")

    def get_string_for_action(self) -> str:
        return "username"
