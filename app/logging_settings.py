import logging


class CustomFormatter(logging.Formatter):
    """Custom formatter with color messages for logging"""

    grey = "\x1b[38;20m"
    blue1 = "\x1b[34;20m"
    blue2 = "\x1b[36;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: blue1 + format + reset,
        logging.INFO: blue2 + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        """For showing message with color and after reset color"""
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class CustomFilter(logging.Filter):
    """Custom filter for logging"""

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname.lower() == "info"


class FileHandler(logging.Handler):
    """Custom handler for writing logs in file"""

    def __init__(self, filename) -> None:
        """Handler constructor for getting filename for writing logs"""
        logging.Handler.__init__(self)
        self.filename = filename

    def emit(self, record: logging.LogRecord) -> None:
        """For writing logs in file"""
        message = self.format(record)
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(message)


# Dict for logging configs
logger_config = {
    "version": 1,
    "filters": {"filter": {"()": CustomFilter}},
    "formatters": {
        "formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
        },
        "color_formatter": {"()": CustomFormatter},
    },
    "handlers": {
        "handler": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "color_formatter",
        },
        "file_handler": {
            "()": FileHandler,
            "level": "WARNING",
            "filename": "app_logs.log",
            "formatter": "formatter",
            "filters": ["filter"],
        },
    },
    "loggers": {
        "app": {"level": "INFO", "handlers": ["handler"]},
        "exceptions": {"level": "ERROR", "handlers": ["handler", "file_handler"]},
    },
}
