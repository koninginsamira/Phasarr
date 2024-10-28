from phasarr.helpers.sql import get_row_count_from
import sqlalchemy as sql

from flask import Blueprint, flash, redirect, request, url_for

from phasarr import db, config, catalog, app
from phasarr.models.user import User
from phasarr.helpers.setup import redirect_setup
from phasarr.forms.setup import AuthSetupForm, DownloadSetupForm, LibrariesSetupForm


setup_app = Blueprint("setup", __name__)


@setup_app.before_request
def before():
    user_count = get_row_count_from(db, User)

    if user_count > 1:
        app.logger.warning(
            "Setup cannot be started with more than one user.")
        
        redirect(url_for("main.main"))


@setup_app.route("/", methods=["GET", "POST"])
def setup():
    redirect_setup(config.setup.stage)

    return redirect(url_for("main.main"))


@setup_app.route("/authentication", methods=["GET", "POST"])
def authentication():
    user = db.session.execute(sql.select(User)).scalar_one_or_none()
    auth_mode = config.authentication.method
    edit_user = bool(user)
    edit_auth_mode = bool(auth_mode)

    form: AuthSetupForm = AuthSetupForm(edit_user=edit_user, edit_auth_mode=edit_auth_mode)

    if request.method == "GET":
        if edit_user:
            form.previous_username.data = user.username
            form.username.data = user.username

        if edit_auth_mode:
            form.auth_method.data = auth_mode

    elif request.method == "POST":
        if form.validate_on_submit():
            new_username = form.username.data
            new_password = form.password.data
            new_auth_mode = form.auth_method.data

            if edit_user:
                if new_username:
                    user.username = new_username
                if new_password:
                    user.set_password(new_password)
            else:
                new_user = User(username=form.username.data)
                new_user.set_password(form.password.data)
                db.session.add(new_user)
            db.session.commit()

            config.authentication.method = new_auth_mode

            config.setup.stage = 1
            
            flash("Setup has been saved!")
            return redirect(url_for("setup.libraries"))
    
    return catalog.render(
        "setup.Authentication",
        skippable=edit_user and edit_auth_mode,
        form=form
    )


@setup_app.route("/libraries", methods=["GET", "POST"])
def libraries():
    form: LibrariesSetupForm = LibrariesSetupForm()

    if form.validate_on_submit():
        new_libraries = []
        
        # User(username=form.username.data)
        # new_user.set_password(form.password.data)
        # db.session.add(new_user)
        # db.session.commit()

        config.setup.stage = 2
        
        flash("Libraries have been configured!")
        return redirect(url_for("setup.download"))
    
    return catalog.render(
        "setup.Libraries",
        form=form
    )


@setup_app.route("/download", methods=["GET", "POST"])
def download():
    form: DownloadSetupForm = DownloadSetupForm()

    if form.validate_on_submit():
        # config.authentication.method = form.auth_method.data

        config.setup.stage = 3
        
        flash("Download has been configured!")
        return redirect(url_for("main.main"))
    
    return catalog.render(
        "setup.Download",
        form=form
    )