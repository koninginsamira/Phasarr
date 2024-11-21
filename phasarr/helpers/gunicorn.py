import logging
import os
from flask import Flask


is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")

def init_gunicorn_logging(app: Flask):
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)