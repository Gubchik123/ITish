from .general import *


def _check_avatar_image_type(form, field: wtforms.FileField) -> None:
    if not field.data.filename.endswith((".png", ".jpg", ".jpeg")):
        raise wtforms.ValidationError()


class UserAvatarForm(FlaskForm):
    avatar_image = wtforms.FileField(
        validators=[
            required,
            _check_avatar_image_type,
        ]
    )
    submit = wtforms.SubmitField("Update avatar")
