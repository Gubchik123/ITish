import flask_login as flog
from flask import Blueprint

from . import funcs


blog = Blueprint("blog", __name__)


@blog.route("/")
def get_all_posts():
    return funcs.get_all_posts()


@blog.route("/tags")
def get_all_tags():
    return funcs.get_all_tags()


@blog.route("/create-post", methods=["GET", "POST"])
@flog.login_required
def create_post():
    return funcs.create_post()


@blog.route("/tag/<tag>")
def get_all_posts_with_(tag: str):
    return funcs.get_all_posts_with_(tag)


@blog.route("/<post_url>")
def get_post_by_(post_url: str):
    return funcs.get_post_by_(post_url)


@blog.route("/<post_url>/like")
@flog.login_required
def like_post_with_(post_url: str):
    return funcs.like_post_with_(post_url)


@blog.route("/<post_url>/comment", methods=["POST"])
@flog.login_required
def comment_post_with_(post_url: str):
    return funcs.comment_post_with_(post_url)


@blog.route("/<post_url>/edit", methods=["GET", "POST"])
@flog.login_required
def edit_post_with_(post_url: str):
    return funcs.edit_post_with_(post_url)
