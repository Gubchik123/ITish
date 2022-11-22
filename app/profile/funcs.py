import flask
import flask_login as flog
from sqlalchemy import desc

from ..app import app
from ..models import User
from ..extensions import db


def _check_if_it_is_current_user(func):
    def inner(username: str):
        return (
            flask.abort(403)
            if flog.current_user.username != username
            else func(username)
        )

    return inner


def get_user_avatar():
    pass


def update_user_avatar():
    pass


def get_user_with_(username: str):
    return flask.render_template(
        "profile/index.html",
        user=User.query.filter(User.username == username).first_or_404(),
    )


@_check_if_it_is_current_user
def delete_user_with_(username: str):
    pass


@_check_if_it_is_current_user
def edit_user_with_(username: str):
    pass
