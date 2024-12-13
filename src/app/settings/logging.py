import logging
import platform
from logging import LogRecord

NEW_LINE_CHAR = '\n' if platform.system() == 'Windows' else '\r'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}][{process}][{module}:{lineno}] {message}',
            'style': '{',
            '()': 'app.settings.logging.Formatter',
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO"
    }
}


class Formatter(logging.Formatter):
    def format(self, record: LogRecord) -> str:
        return super(Formatter, self).format(record).replace('\n', NEW_LINE_CHAR)

logger = logging.getLogger()