from flask_sqlalchemy import SQLAlchemy

from .app import app


### Flask-SQLAlchemy ###
db = SQLAlchemy(app)
