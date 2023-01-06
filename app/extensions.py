import flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_login import LoginManager

from .db import db
from .app import app


### Flask-Migrate ###
migrate = Migrate(app, db)


### Flask-Login ###
from .models import User, Post, Tag, Like, Comment

login_manager = LoginManager(app)

login_manager.login_view = "auth.log_in_user"
login_manager.login_message = "Please log in to access this page"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def _load_user(id):
    """For getting user from db if exist"""
    try:
        return User.query.filter(User.id == id).first()
    except:
        flask.flash("Sorry, there was the error. Try again", category="error")
        flask.redirect("/")


### Flask-Admin ###
from .admin import *


admin = Admin(
    app, "ITish", url="/admin/", index_view=HomeAdminView(), template_mode="bootstrap4"
)

admin.add_view(UserAdminView(User, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(LikeAdminView(Like, db.session))
admin.add_view(CommentAdminView(Comment, db.session))
