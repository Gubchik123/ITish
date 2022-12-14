import flask
import flask_login as flog
from werkzeug.security import generate_password_hash

from ..extensions import db
from ..exceptions import catch_sqlalchemy_errors
from .forms import NewEmailForm, NewUsernameForm, NewPasswordForm


@catch_sqlalchemy_errors
def _update_current_user_avatar_in_db() -> None:
    """For updating user avatar in db with data from file field"""
    flog.current_user.avatar = flask.request.files["avatar_image"].read()
    db.session.commit()


@catch_sqlalchemy_errors
def _delete_current_user_posts_from_db():
    """For deleting current user posts before deleting current user"""
    for post in flog.current_user.posts.all():
        db.session.delete(post)
    db.session.commit()


@catch_sqlalchemy_errors
def _delete_current_user_from_db() -> None:
    """For deleting current user from database"""
    _delete_current_user_posts_from_db()

    db.session.delete(flog.current_user)
    db.session.commit()


@catch_sqlalchemy_errors
def _edit_current_user_email_in_db() -> None:
    """For editing user email in database with data from new email form"""
    flog.current_user.email = NewEmailForm().email.data
    db.session.commit()


@catch_sqlalchemy_errors
def _edit_current_user_username_in_db() -> None:
    """For editing user username in database with data from new username form"""
    flog.current_user.username = NewUsernameForm().username.data
    db.session.commit()


@catch_sqlalchemy_errors
def _edit_current_user_password_in_db() -> None:
    """For editing user password in database with data from new password form"""
    flog.current_user.password = generate_password_hash(NewPasswordForm().password.data)
    db.session.commit()
