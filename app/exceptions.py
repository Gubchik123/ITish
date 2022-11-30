import logging
import logging.config
from typing import NamedTuple

import flask
from sqlalchemy.exc import SQLAlchemyError
from jinja2.exceptions import TemplateError
from werkzeug.routing.exceptions import RoutingException

from .logging_settings import logger_config


# Set up logging config
logging.config.dictConfig(logger_config)

# Creating my logger
logger = logging.getLogger("exceptions")


class Error(NamedTuple):
    """NamedTuple for storing information about error"""

    code = 500
    name: str
    description: str


def _render_error_page(error: Error) -> tuple[str, int]:
    """For rendering error template with error"""
    return (
        flask.render_template(
            "error.html",
            error=error,
        ),
        error.code,
    )


def catch_sqlalchemy_errors(func):
    """The decorator for catching SQAlchemy errors"""

    def inner(*args, **kwargs):
        try:
            answer = func(*args, **kwargs)
        except SQLAlchemyError as e:
            logger.error(f"Exception with SQLAlchemy: {e}")
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
    """The decorator for catching template or build flask errors"""

    def decorator(func):
        def inner(*args, **kwargs):
            try:
                answer = func(*args, **kwargs)
            except flask_exception as e:
                logger.error(f"Flask exception with: {e}")
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
