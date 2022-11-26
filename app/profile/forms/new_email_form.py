from .general import *
from .general import _get_striped_


def _check_email(form, field):
    if User.query.filter(User.email == _get_striped_(field.data)).first():
        raise wtf.ValidationError("There is the user with such email!")


class NewEmailForm(FlaskForm):
    email = wtf.EmailField(
        "Email",
        validators=[
            required,
            validator.Email("Enter the correct email!"),
            validator.Length(min=10, max=255),
            _check_email,
        ],
    )
    submit = wtf.SubmitField("Change email")

    def get_string_for_action(self) -> str:
        return "email"
