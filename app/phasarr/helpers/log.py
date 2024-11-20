import logging
from logging.config import dictConfig
from flask import Flask


def init_logging():
    # dictConfig({
    #     'version': 1,
    #     'formatters': {'default': {
    #         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    #     }},
    #     'root': {
    #         'level': 'INFO'
    #     }
    # })

    werkzeug_logger = logging.getLogger("werkzeug")

    


def log_to_stdout(app: Flask):
    pass
    # app.logger
    # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    # app.logger.disabled = False
    # app.logger.setLevel(logging.DEBUG)
    # app.logger.handlers = werkzeug_logger.handlers
    # werkzeug_logger.setLevel(logging.DEBUG)  # Adjust as necessary


def log_to_gunicorn(app: Flask):
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)