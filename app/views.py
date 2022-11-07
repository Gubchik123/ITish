from . import funcs
from .app import app


@app.route("/")
def get_home_page():
    return funcs.get_home_page()
