from auth import auth
from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route("/")
@auth.login_required
def index():
    return render_template("index.html")