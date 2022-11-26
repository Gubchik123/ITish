from .general import *


def _check_avatar_image_type(form, field):
    if not field.data.filename.endswith((".png", ".jpg", ".jpeg")):
        raise wtf.ValidationError()


class UserAvatarForm(FlaskForm):
    avatar_image = wtf.FileField(
        validators=[
            required,
            _check_avatar_image_type,
        ]
    )
    submit = wtf.SubmitField("Update avatar")
