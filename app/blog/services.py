from flask_login import current_user

from ..extensions import db
from ..models import Tag, Post, Like, Comment
from ..exceptions import catch_sqlalchemy_errors
from .forms import PostCreateForm, PostEditForm, CommentForm


@catch_sqlalchemy_errors
def _delete_from_db_(item: Post | Like | Comment) -> None:
    """For deleting an item (Post, Like or Comment) from database"""
    db.session.delete(item)
    db.session.commit()


@catch_sqlalchemy_errors
def _add_in_db_(item: Post | Like | Comment) -> None:
    """For adding an item (Post, Like or Comment) in database"""
    db.session.add(item)
    db.session.commit()


def _there_is_not_tag_with_such_(title: str) -> bool:
    """For checking on exist tag by tag title"""
    return not Tag.query.filter(Tag.title == title).first()


@catch_sqlalchemy_errors
def _create_non_existent_tags_from_(tag_titles: list[str]) -> None:
    """For creating non existent tags in database"""
    for tag_title in tag_titles:
        if _there_is_not_tag_with_such_(tag_title):
            db.session.add(Tag(title=tag_title))
    db.session.commit()


def _get_striped_and_lower_tag_titles_from_(
    form: PostCreateForm | PostEditForm,
) -> list[str]:
    """For getting list of tag titles from post creating or editing form"""
    striped_and_lower_tag_titles = [
        tag_title.strip().lower() for tag_title in form.post_tags.data.split(",")
    ]
    _create_non_existent_tags_from_(striped_and_lower_tag_titles)
    return striped_and_lower_tag_titles


def _get_all_tags_for_post_from_(form: PostCreateForm | PostEditForm) -> list[Tag]:
    """For getting list of tags for post"""
    return (
        [
            Tag.query.filter(Tag.title == tag_title).first()
            for tag_title in _get_striped_and_lower_tag_titles_from_(form)
        ]
        if form.post_tags.data
        else []
    )


@catch_sqlalchemy_errors
def _add_post_in_db_with_data_from_(form: PostCreateForm) -> Post:
    """For adding a post in database with data from post creating form"""
    post = Post(
        title=form.post_title.data,
        body=form.post_body.data,
        user_id=current_user.id,
        tags=_get_all_tags_for_post_from_(form),
    )
    _add_in_db_(post)
    return post


@catch_sqlalchemy_errors
def _add_comment_in_db_for_(post: Post) -> None:
    """For adding a comment for post in database with data from comment form"""
    _add_in_db_(
        Comment(
            body=CommentForm().comment_body.data,
            user_id=current_user.id,
            post_id=post.id,
        )
    )


@catch_sqlalchemy_errors
def _edit_post_in_db_with_data_from_(form: PostEditForm, post: Post) -> None:
    """For editing post by data from post editing form"""
    post.title = form.post_title.data
    post.body = form.post_body.data
    post.tags = _get_all_tags_for_post_from_(form)
    db.session.commit()
