import flask
import flask_login as flog
from sqlalchemy import desc

from ..app import app
from ..extensions import db
from ..models import Post, Tag, Comment, Like
from .forms import PostCreateForm, PostEditForm, CommentForm


def get_js_file(filename: str):
    return flask.send_from_directory(
        app.config["UPLOAD_FOLDER"],
        f"js/{filename}" if ".js" in filename else f"js/{filename}.js",
        as_attachment=True,
        mimetype="text/javascript",
    )


def get_blog_page():
    tab = flask.request.args.get("tab")
    tab = tab if tab else "posts"

    return (
        _get_all_posts()
        if tab == "posts"
        else (_get_all_tags() if tab == "tags" else flask.abort(404))
    )


def _get_posts_with_pagination():
    q = flask.request.args.get("q", "")

    page = flask.request.args.get("page", "")
    page = (int(page) if page.isdigit() else -1) if page else 1

    posts = (
        Post.query
        if not q
        else Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
    )
    return posts.order_by(Post.created.desc()).paginate(page=page, per_page=5)


def _get_all_posts():
    return flask.render_template(
        "blog/all_posts.html", posts=_get_posts_with_pagination()
    )


def _get_all_tags():
    return flask.render_template(
        "blog/all_tags.html", tags=Tag.query.order_by(Tag.url).all()
    )


def _create_non_existent_tags_from_(titles: list[str]):
    for tag_title in titles:
        if not Tag.query.filter(Tag.title == tag_title).first():
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
        for tag_title in _get_striped_and_lower_tag_titles_from_(form)
    ]


def _edit_post_in_db_with_data_from_(form: PostCreateForm):
    db.session.add(
        Post(
            title=form.post_title.data,
            body=form.post_body.data,
            user_id=flog.current_user.id,
            tags=_get_all_tags_for_post_from_(form),
        )
    )
    db.session.commit()


def create_post():
    form = PostCreateForm()

    if form.validate_on_submit():
        _edit_post_in_db_with_data_from_(form)
        flask.flash("Post has successfully added", category="success")

    return flask.render_template("blog/create_post.html", form=form)


def get_all_posts_with_(tag: str):
    return flask.render_template(
        "blog/tag.html", tag=Tag.query.filter(Tag.url == tag).first_or_404()
    )


def get_post_by_(post_url: str):
    return flask.render_template(
        "blog/post.html",
        desc=desc,
        form=CommentForm(),
        post=Post.query.filter(Post.url == post_url).first_or_404(),
    )


def _get_post_id_and_like_from_json() -> tuple[int, Like]:
    data = flask.request.get_json()
    post_id = data["post_id"]

    return (
        post_id,
        Like.query.filter(
            Like.user_id == data["user_id"], Like.post_id == post_id
        ).first(),
    )


def like_post():
    post_id, like = _get_post_id_and_like_from_json()

    if like:
        db.session.delete(like)
        response = "Like was deleted"
    else:
        db.session.add(Like(user_id=flog.current_user.id, post_id=post_id))
        response = "Like was added"

    db.session.commit()
    return response


def _add_comment_in_db_for_post_with_(post_url: str):
    form = CommentForm()
    post = Post.query.filter(Post.url == post_url).first()

    db.session.add(
        Comment(
            body=form.comment_body.data, user_id=flog.current_user.id, post_id=post.id
        )
    )
    db.session.commit()


def comment_post_with_(post_url: str):
    _add_comment_in_db_for_post_with_(post_url)
    flask.flash("Comment has successfully added", category="success")
    return flask.redirect(flask.url_for("blog.get_post_by_", post_url=post_url))


def _check_if_current_user_is_author_of_(content):
    if content.user.id != flog.current_user.id:
        flask.abort(403)


def delete_comment_with_(post_url: str, comment_id: int):
    comment = Comment.query.filter(Comment.id == comment_id).first()

    _check_if_current_user_is_author_of_(comment)

    db.session.delete(comment)
    db.session.commit()

    flask.flash("Comment has successfully deleted", category="success")
    return flask.redirect(flask.url_for("blog.get_post_by_", post_url=post_url))


def _edit_post_in_db_with_data_from_(form: PostEditForm, post: Post):
    post.title = form.post_title.data
    post.body = form.post_body.data
    post.tags = _get_all_tags_for_post_from_(form)
    db.session.commit()


def edit_post_with_(post_url: str):
    form = PostEditForm()
    post = Post.query.filter(Post.url == post_url).first_or_404()

    _check_if_current_user_is_author_of_(post)

    if form.validate_on_submit():
        _edit_post_in_db_with_data_from_(form, post)

        flask.flash("Post has successfully edited", category="success")
        return flask.redirect(flask.url_for("blog.get_post_by_", post_url=post_url))

    return flask.render_template("blog/edit_post.html", form=form, post=post)
