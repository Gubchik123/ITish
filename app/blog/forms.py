import wtforms as wtf
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length


class _PostProcessingForm(FlaskForm):
    """General form for post creating and editing"""

    post_title = wtf.StringField()
    post_body = wtf.TextAreaField()
    post_tags = wtf.StringField("Post tags (optional)")


class PostCreateForm(_PostProcessingForm):
    """Form for post creating"""

    post_submit = wtf.SubmitField("Add post")


class PostEditForm(_PostProcessingForm):
    """Form for post editing"""

    post_submit = wtf.SubmitField("Edit post")


class CommentForm(FlaskForm):
    """Form for post commenting"""

    comment_body = wtf.TextAreaField(
        "Write your comment...",
        validators=[InputRequired("The area must be filled!"), Length(min=5)],
    )
    submit = wtf.SubmitField("Add comment")
