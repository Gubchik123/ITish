import flask
from jinja2.exceptions import TemplateError
from werkzeug.routing.exceptions import RoutingException

from .exceptions import catch_flask_error_


@catch_flask_error_(TemplateError)
def render_template(path: str, **kwargs) -> str:
    return flask.render_template(path, **kwargs)


@catch_flask_error_(RoutingException)
def redirect_to_url_for_(path: str, **kwargs) -> flask.Response:
    return flask.redirect(flask.url_for(path, **kwargs))


def get_home_page() -> str:
    return render_template("index.html")


def get_FAQs_page() -> str:
    return render_template("FAQs.html")


def get_about_page() -> str:
    return render_template("about.html")


def _get_logout_page_url() -> str:
    return flask.request.url_root[:-1] + flask.url_for("auth.log_out_user")


def abort_to_login_page() -> flask.Response:
    next = flask.request.url if flask.request.url != _get_logout_page_url() else None
    flask.flash("Please log in to access this page", category="warning")
    return redirect_to_url_for_("auth.log_in_user", next=next)


def get_error_page(error) -> tuple[str, int]:
    return (render_template("error.html", error=error), error.code)
