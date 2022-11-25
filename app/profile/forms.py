import re

import wtforms as wtf
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


def _check_avatar_image_type(form, field):
    if not field.data.filename.endswith((".png", ".jpg", ".jpeg")):
        raise wtf.ValidationError()


class UserAvatarForm(FlaskForm):
    avatar_image = wtf.FileField(
        validators=[
            InputRequired(),
            _check_avatar_image_type,
        ]
    )
    submit = wtf.SubmitField("Update avatar")
