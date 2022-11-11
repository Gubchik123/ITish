import flask_login as flog
from flask import Blueprint

from . import funcs


blog = Blueprint("blog", __name__)