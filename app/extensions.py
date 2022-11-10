from flask_admin import Admin
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .app import app


db = SQLAlchemy(app)

migrate = Migrate(app, db)

# admin = Admin(app)


### Flask-Login ###
from . import models

login_manager = LoginManager(app)

login_manager.login_view = "auth.log_in_user"
login_manager.login_message = "Please log in to access this page"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def _load_user(id):
    return models.User.query.filter(models.User.id == id).first()
