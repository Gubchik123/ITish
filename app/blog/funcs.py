import flask
import flask_login as flog


def get_all_posts():
    pass


def get_all_tags():
    pass


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
