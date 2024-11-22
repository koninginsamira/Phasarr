from flask import flash, redirect, url_for

from phasarr import config, catalog
from phasarr.setup import setup_app, stages
from phasarr.setup.forms import DownloadSetupForm
from phasarr.components.auth.decorators.auth import login_required


@setup_app.route("/download", methods=["GET", "POST"])
@login_required
def download():
    form: DownloadSetupForm = DownloadSetupForm()

    config.setup.stage = 2

    if form.validate_on_submit():
        # config.authentication.method = form.auth_method.data

        config.setup.stage = 3
        
        flash("Download has been configured!")
        return redirect(url_for("main.main"))
    
    return catalog.render(
        "setup.Download",
        current_stage="download",
        stages=stages,
        form=form
    )