import flask
from jinja2.exceptions import TemplateError
from werkzeug.routing.exceptions import RoutingException

from .exceptions import catch_flask_error_, catch_all_other_exceptions


@catch_all_other_exceptions
@catch_flask_error_(TemplateError)
def render_template(path: str, **kwargs) -> str:
    """For rendering the template by the given path"""
    return flask.render_template(path, **kwargs)


@catch_all_other_exceptions
@catch_flask_error_(RoutingException)
def redirect_to_url_for_(path: str, **kwargs) -> flask.Response:
    """For redirecting to the given path"""
    return flask.redirect(flask.url_for(path, **kwargs))


def get_home_page() -> str:
    """For rendering the template for the 'Home' page"""
    return render_template("index.html")


def get_FAQs_page() -> str:
    """For rendering the template for the 'FAQs' page"""
    return render_template("FAQs.html")


def _get_logout_page_url() -> str:
    """For getting url to the user logout page"""
    return flask.request.url_root[:-1] + flask.url_for("auth.log_out_user")


def redirect_to_login_page() -> flask.Response:
    """For redirecting to the user login page"""
    next = flask.request.url if flask.request.url != _get_logout_page_url() else None
    flask.flash("Please log in to access this page", category="warning")
    return redirect_to_url_for_("auth.log_in_user", next=next)


def get_error_page(error) -> tuple[str, int]:
    """For rendering the template for the error page"""
    return (render_template("error.html", error=error), error.code)
