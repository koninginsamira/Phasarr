from phasarr.helpers.auth import login_required
from flask import Blueprint, render_template


main_app = Blueprint('main', __name__)


@main_app.route("/")
@login_required
def main():
    return render_template("index.html")