import os
from auth import auth_app
from main import main
from setup import setup
from api import api
from helpers.debug import attach_debugpy
from helpers.log import init_gunicorn_logging
from flask import Flask


app = Flask(__name__)
app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(setup, url_prefix='/setup')
app.register_blueprint(api, url_prefix='/api')


if __name__ != '__main__':
    init_gunicorn_logging(app)


if os.environ["FLASK_ENV"] == "development":
    attach_debugpy(app)