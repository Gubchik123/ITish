import flask
import flask_login as flog

from ..models import Post, Tag


def get_blog_page():
    tab = flask.request.args.get("tab")
    tab = tab if tab else "posts"

    return (
        _get_all_posts()
        if tab == "posts"
        else (_get_all_tags() if tab == "tags" else flask.abort(404))
    )


def _get_all_posts():
    return flask.render_template(
        "blog/all_posts.html", posts=Post.query.order_by(Post.created.desc()).all()
    )


def _get_all_tags():
    return flask.render_template(
        "blog/all_tags.html", tags=Tag.query.order_by(Tag.url).all()
    )


@flog.login_required
def create_post():
    pass


def get_all_posts_with_(tag: str):
    pass


def get_post_by_(post_url: str):
    pass


@flog.login_required
def like_post_with_(post_url: str):
    pass


@flog.login_required
def comment_post_with_(post_url: str):
    pass


@flog.login_required
def edit_post_with_(post_url: str):
    pass
