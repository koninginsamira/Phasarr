from phasarr import catalog
from phasarr.main import main_app
from phasarr.components.auth.decorators.auth import login_required


@main_app.before_request
@login_required
def before():
    pass


@main_app.route("/")
def main():
    return catalog.render(
        "main.Main"
    )