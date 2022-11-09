from . import funcs
from .app import app

from .auth import blueprint


app.register_blueprint(blueprint.auth, url_prefix="/auth")


@app.route("/")
def get_home_page():
    return funcs.get_home_page()


@app.route("/FAQs")
def get_FAQs_page():
    return funcs.get_FAQs_page()


@app.route("/about")
def get_about_page():
    return funcs.get_about_page()


@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(501)
def get_error_page(error):
    return funcs.get_error_page(error)
