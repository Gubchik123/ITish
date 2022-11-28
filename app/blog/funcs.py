import flask
import flask_login as flog
from sqlalchemy import desc
from werkzeug.routing.exceptions import RoutingException

from ..app import app
from ..exceptions import catch_flask_error_
from ..models import Post, Tag, Comment, Like
from ..funcs import render_template, redirect_to_url_for_

from . import services
from .forms import PostCreateForm, PostEditForm, CommentForm


def get_js_file(filename: str):
    return flask.send_from_directory(
        app.config["UPLOAD_FOLDER"],
        f"js/{filename}" if ".js" in filename else f"js/{filename}.js",
        as_attachment=True,
        mimetype="text/javascript",
    )


def get_blog_page():
    tab = flask.request.args.get("tab", "posts")

    return (
        _get_all_posts()
        if tab == "posts"
        else (_get_all_tags() if tab == "tags" else flask.abort(404))
    )


@services.catch_sqlalchemy_errors
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
    return render_template("blog/all_posts.html", posts=_get_posts_with_pagination())


@services.catch_sqlalchemy_errors
def _get_all_tags():
    return render_template("blog/all_tags.html", tags=Tag.query.order_by(Tag.url).all())


@services.catch_sqlalchemy_errors
def _there_is_post_with_such_(title: str) -> bool:
    return bool(Post.query.filter(Post.title == title).first())


def create_post():
    form = PostCreateForm()

    if form.validate_on_submit():
        if _there_is_post_with_such_(form.post_title.data):
            flask.flash("Error! There is the post with such title!", category="danger")
        else:
            services._add_post_in_db_with_data_from_(form)
            flask.flash("Post has successfully added", category="success")

    return render_template("blog/create_post.html", form=form)


@services.catch_sqlalchemy_errors
def get_all_posts_with_(tag: str):
    return render_template(
        "blog/tag.html", tag=Tag.query.filter(Tag.url == tag).first_or_404()
    )


@services.catch_sqlalchemy_errors
def get_post_by_(post_url: str):
    return render_template(
        "blog/post.html",
        desc=desc,
        form=CommentForm(),
        post=Post.query.filter(Post.url == post_url).first_or_404(),
    )


def _check_if_current_user_is_author_of_(content):
    if content.user.id != flog.current_user.id:
        flask.abort(403)


@services.catch_sqlalchemy_errors
@catch_flask_error_(RoutingException)
def delete_post_with_(post_url: str):
    post = Post.query.filter(Post.url == post_url).first_or_404()

    _check_if_current_user_is_author_of_(post)

    services._delete_from_db_(post)

    flask.flash("Post has successfully deleted", category="success")
    return flask.redirect(
        flask.request.args.get("next") or flask.url_for("blog.get_blog_page")
    )


@services.catch_sqlalchemy_errors
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
        services._delete_from_db_(like)
        response = "Like was deleted"
    else:
        services._add_in_db_(Like(user_id=flog.current_user.id, post_id=post_id))
        response = "Like was added"

    return response


@services.catch_sqlalchemy_errors
def comment_post_with_(post_url: str):
    services._add_comment_in_db_for_(Post.query.filter(Post.url == post_url).first())

    flask.flash("Comment has successfully added", category="success")
    return redirect_to_url_for_("blog.get_post_by_", post_url=post_url)


@services.catch_sqlalchemy_errors
@catch_flask_error_(RoutingException)
def delete_comment_with_(post_url: str, comment_id: int):
    comment = Comment.query.filter(Comment.id == comment_id).first_or_404()

    _check_if_current_user_is_author_of_(comment)
    services._delete_from_db_(comment)

    flask.flash("Comment has successfully deleted", category="success")
    return flask.redirect(
        flask.request.args.get("next")
        or flask.url_for("blog.get_post_by_", post_url=post_url)
    )


@services.catch_sqlalchemy_errors
def edit_post_with_(post_url: str):
    form = PostEditForm()
    post = Post.query.filter(Post.url == post_url).first_or_404()

    _check_if_current_user_is_author_of_(post)

    if form.validate_on_submit():
        services._edit_post_in_db_with_data_from_(form, post)

        flask.flash("Post has successfully edited", category="success")
        return redirect_to_url_for_("blog.get_post_by_", post_url=post_url)

    return render_template("blog/edit_post.html", form=form, post=post)
