from phasarr import config
from phasarr.setup import setup_app, stages
from phasarr.components.utilities.helpers.setup import redirect_setup


@setup_app.route("/", methods=["GET", "POST"])
def setup():
    current_stage = config.setup.stage

    return redirect_setup(current_stage, stages, "main.main")