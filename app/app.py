from flask import Flask

from . import views
from . import config
from . import extensions


app = Flask(__name__)
app.config.from_object(config.ForProduction)
