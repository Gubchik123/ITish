import os 
import hmac
import hashlib
import subprocess

import flask
from jinja2.exceptions import TemplateError
from werkzeug.routing.exceptions import RoutingException

from .config import BASE_DIR
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


def get_feedback_page() -> str:
    """For rendering the template for the 'Feedback' page"""
    return render_template("feedback.html")


def get_robots_txt() -> str:
    """For getting special content to stop bots from crawling."""
    return """
        User-agent: *
        Disallow: /
    """.replace("        ", "").strip()


def _is_valid_signature(x_hub_signature, data, private_key):
    """
    For checking if the signature is valid
    :param x_hub_signature and data: The signature from the webhook payload header
    :param private_key: The webhook secret
    :return: True if the signature is valid, False otherwise
    """
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)


def update_server_webhook() -> str:
    """For updating the server with a webhook."""
    x_hub_signature = flask.request.headers.get("X-Hub-Signature")
    w_secret = os.getenv("WEBHOOK_SECRET")
    if x_hub_signature is None:
        return "No signature given", 401
    if not _is_valid_signature(x_hub_signature, flask.request.data, w_secret):
        return "Invalid signature", 401
    os.chdir(BASE_DIR)
    subprocess.run(["git", "pull"])
    return "Updated PythonAnywhere successfully", 200


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
