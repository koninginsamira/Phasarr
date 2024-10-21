from flask import Blueprint


setup_app = Blueprint('setup', __name__)


@setup_app.route("/")
def index():
    return "setup"