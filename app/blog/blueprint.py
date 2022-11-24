import flask_login as flog
from flask import Blueprint

from . import funcs


blog = Blueprint("blog", __name__)


@blog.route("/js-file/<path:filename>")
def get_js_file(filename: str):
    return funcs.get_js_file(filename)


@blog.route("/")
def get_blog_page():
    return funcs.get_blog_page()


@blog.route("/create-post", methods=["GET", "POST"])
@flog.login_required
def create_post():
    return funcs.create_post()


@blog.route("/tag/<tag>")
def get_all_posts_with_(tag: str):
    return funcs.get_all_posts_with_(tag)


@blog.route("/post/<post_url>")
def get_post_by_(post_url: str):
    return funcs.get_post_by_(post_url)


@blog.route("/post/<post_url>/delete")
@flog.login_required
def delete_post_with_(post_url: str):
    return funcs.delete_post_with_(post_url)


@blog.route("/post/<post_url>/like", methods=["POST"])
@flog.login_required
def like_post_with_(post_url: str):
    return funcs.like_post()


@blog.route("/post/<post_url>/comment", methods=["POST"])
@flog.login_required
def comment_post_with_(post_url: str):
    return funcs.comment_post_with_(post_url)


@blog.route("/post/<post_url>/delete-comment/<int:comment_id>")
@flog.login_required
def delete_comment_with_(post_url: str, comment_id: int):
    return funcs.delete_comment_with_(post_url, comment_id)


@blog.route("/post/<post_url>/edit", methods=["GET", "POST"])
@flog.login_required
def edit_post_with_(post_url: str):
    return funcs.edit_post_with_(post_url)
