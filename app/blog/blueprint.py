import flask
import flask_login as flog

from . import funcs


blog = flask.Blueprint("blog", __name__)


@blog.route("/js-file/<path:filename>")
def get_js_file(filename: str) -> flask.Response:
    """For getting js file from 'static' folder"""
    return funcs.get_js_file(filename)


@blog.route("/")
def get_blog_page() -> str:
    """For getting the 'blog' page"""
    return funcs.get_blog_page()


@blog.route("/create-post", methods=["GET", "POST"])
@flog.login_required
def create_post() -> str:
    """
    GET: getting the page for creating post
    POST: creating post
    """
    return funcs.create_post()


@blog.route("/tag/<tag>")
def get_all_posts_with_(tag: str) -> str:
    """For getting all posts by tag"""
    return funcs.get_all_posts_with_(tag)


@blog.route("/post/<post_url>")
def get_post_by_(post_url: str) -> str:
    """For getting the post page"""
    return funcs.get_post_by_(post_url)


@blog.route("/post/<post_url>/delete")
@flog.login_required
def delete_post_with_(post_url: str) -> flask.Response:
    """For deleting post by post url"""
    return funcs.delete_post_with_(post_url)


@blog.route("/post/<post_url>/like", methods=["POST"])
@flog.login_required
def like_post_with_(post_url: str) -> str:
    """For getting json with data for post liking"""
    return funcs.like_post()


@blog.route("/post/<post_url>/comment", methods=["POST"])
@flog.login_required
def comment_post_with_(post_url: str) -> flask.Response:
    """For post commenting"""
    return funcs.comment_post_with_(post_url)


@blog.route("/post/<post_url>/delete-comment/<int:comment_id>")
@flog.login_required
def delete_comment_with_(post_url: str, comment_id: int) -> flask.Response:
    """For deleting comment by id for post by post url"""
    return funcs.delete_comment_with_(post_url, comment_id)


@blog.route("/post/<post_url>/edit", methods=["GET", "POST"])
@flog.login_required
def edit_post_with_(post_url: str) -> str | flask.Response:
    """
    GET: getting the page for post editing
    POST: post editing
    """
    return funcs.edit_post_with_(post_url)
