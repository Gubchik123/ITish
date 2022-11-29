from .general import *


def _check_avatar_image_type(form, field: wtforms.FileField) -> None:
    """For checking on valid ending of file from file field"""
    if not field.data.filename.endswith((".png", ".jpg", ".jpeg")):
        raise wtforms.ValidationError()


class UserAvatarForm(FlaskForm):
    """Form for updating user avatar"""

    avatar_image = wtforms.FileField(
        validators=[
            required,
            _check_avatar_image_type,
        ]
    )
    submit = wtforms.SubmitField("Update avatar")
