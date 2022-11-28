from typing import NamedTuple

import flask
from sqlalchemy.exc import SQLAlchemyError
from jinja2.exceptions import TemplateError
from werkzeug.routing.exceptions import RoutingException


class Error(NamedTuple):
    code = 500
    name: str
    description: str


def _render_error_page(error: Error):
    return (
        flask.render_template(
            "error.html",
            error=error,
        ),
        error.code,
    )


def catch_sqlalchemy_errors(func):
    def inner(*args, **kwargs):
        try:
            answer = func(*args, **kwargs)
        except SQLAlchemyError:
            answer = _render_error_page(
                error=Error(
                    name="DB error",
                    description="""
                        Sorry for the inconvenience, but an error occurred while 
                        working with data and databases. Check your Internet 
                        connection or try later.
                    """,
                ),
            )
        finally:
            return answer

    return inner


def catch_flask_error_(flask_exception: TemplateError | RoutingException):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                answer = func(*args, **kwargs)
            except flask_exception:
                print("catch exception")
                answer = _render_error_page(
                    error=Error(
                        name="Page error",
                        description="""
                            Sorry for the inconvenience, but there was an error 
                            retrieving the page. Try again later.
                        """,
                    ),
                )
            finally:
                return answer

        return inner

    return decorator
