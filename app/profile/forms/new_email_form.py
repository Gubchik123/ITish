from .general import *
from .general import _get_striped_


def _there_is_user_with_such_email(email: str) -> bool:
    return bool(User.query.filter(User.email == email).first())


def _check_email(form, field):
    if _there_is_user_with_such_email(_get_striped_(field.data)):
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
