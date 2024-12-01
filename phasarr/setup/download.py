import os
from flask import flash, redirect, request, url_for, current_app as app
from werkzeug.datastructures import FileStorage

from phasarr import config, catalog
from phasarr.variables import config_folder
from phasarr.setup import setup_app, stages
from phasarr.setup.forms import DownloadSetupForm
from phasarr.components.auth.decorators.auth import login_required


@setup_app.route("/download", methods=["GET", "POST"])
@login_required
def download():
    form: DownloadSetupForm = DownloadSetupForm()

    config.setup.stage = 2

    match request.method:
        case "GET":
            pass

        case "POST":
            if form.validate_on_submit():
                cookies = form.cookies.data

                if cookies:
                    filename = "cookies.txt"
                    path = os.path.join(config_folder, filename)

                    cookies.save(path)
                    app.logger.info("New cookies file has been uploaded.")

                config.setup.stage = 3
                
                flash("Download has been configured!")
                return redirect(url_for("main.main"))
    
    return catalog.render(
        "setup.Download",
        current_stage="download",
        stages=stages,
        form=form
    )