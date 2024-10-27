from flask import redirect, url_for

from phasarr import config


def redirect_setup():
    match config.setup.stage:
        case 0:
            return redirect(url_for("setup.authentication"))
        case 1:
            return redirect(url_for("setup.libraries"))
        case 2:
            return redirect(url_for("setup.download"))