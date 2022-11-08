from flask_admin import Admin
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .app import app


db = SQLAlchemy(app)

migrate = Migrate(app, db)

# admin = Admin(app)
# login_manager = LoginManager(app)
