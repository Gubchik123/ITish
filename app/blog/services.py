from flask_login import current_user

from ..extensions import db
from ..models import Post, Tag, Comment
from .forms import PostCreateForm, PostEditForm, CommentForm


def _delete_from_db_(item):
    db.session.delete(item)
    db.session.commit()


def _add_in_db_(item):
    db.session.add(item)
    db.session.commit()


def _there_is_not_tag_with_such_(title: str) -> bool:
    return not Tag.query.filter(Tag.title == title).first()


def _create_non_existent_tags_from_(tag_titles: list[str]):
    for tag_title in tag_titles:
        if _there_is_not_tag_with_such_(tag_title):
            db.session.add(Tag(title=tag_title))
    db.session.commit()


def _get_striped_and_lower_tag_titles_from_(
    form: PostCreateForm | PostEditForm,
) -> list[str]:
    return [tag_title.strip().lower() for tag_title in form.post_tags.data.split(",")]


def _get_all_tags_for_post_from_(form: PostCreateForm | PostEditForm):
    if not form.post_tags.data:
        return []

    striped_and_lower_tag_titles = _get_striped_and_lower_tag_titles_from_(form)

    _create_non_existent_tags_from_(striped_and_lower_tag_titles)

    return [
        Tag.query.filter(Tag.title == tag_title).first()
        for tag_title in striped_and_lower_tag_titles
    ]


def _add_post_in_db_with_data_from_(form: PostCreateForm):
    db.session.add(
        Post(
            title=form.post_title.data,
            body=form.post_body.data,
            user_id=current_user.id,
            tags=_get_all_tags_for_post_from_(form),
        )
    )
    db.session.commit()


def _add_comment_in_db_for_(post: Post):
    db.session.add(
        Comment(
            body=CommentForm().comment_body.data,
            user_id=current_user.id,
            post_id=post.id,
        )
    )
    db.session.commit()


def _edit_post_in_db_with_data_from_(form: PostEditForm, post: Post):
    post.title = form.post_title.data
    post.body = form.post_body.data
    post.tags = _get_all_tags_for_post_from_(form)
    db.session.commit()