import wtforms as wtf
from flask_wtf import FlaskForm


class _PostProcessingForm(FlaskForm):
    post_title = wtf.StringField()
    post_body = wtf.TextAreaField()
    post_tags = wtf.StringField("Post tags (optional)")


class PostCreateForm(_PostProcessingForm):
    post_submit = wtf.SubmitField("Add post")


class PostEditForm(_PostProcessingForm):
    post_submit = wtf.SubmitField("Edit post")
