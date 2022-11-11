from . import funcs
from .app import app

from .auth.blueprint import auth
from .blog.blueprint import blog


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(blog, url_prefix="/blog")


@app.route("/")
def get_home_page():
    return funcs.get_home_page()


@app.route("/FAQs")
def get_FAQs_page():
    return funcs.get_FAQs_page()


@app.route("/about")
def get_about_page():
    return funcs.get_about_page()


@app.errorhandler(401)
def abort_to_login_page(error):
    return funcs.abort_to_login_page()


@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(501)
def get_error_page(error):
    return funcs.get_error_page(error)
