import sqlalchemy as sql

from flask_login import current_user
from flask import Blueprint, flash, redirect, url_for

from phasarr import db, config, catalog
from phasarr.models.user import User
from phasarr.forms.setup import AuthenticationSetupForm, DownloadSetupForm, LibrariesSetupForm

setup_app = Blueprint("setup", __name__)

@setup_app.route("/", methods=["GET", "POST"])
def setup():
    return redirect(url_for("setup.authentication"))

@setup_app.route("/authentication", methods=["GET", "POST"])
def authentication():
    user_exists = db.session.execute(sql.select(User)).first()

    if not user_exists:
        # if current_user.is_authenticated:
        #     return redirect(url_for("main.main"))
        
        form: AuthenticationSetupForm = AuthenticationSetupForm()

        if form.validate_on_submit():
            new_user = User(username=form.username.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()

            config.authentication.method = form.auth_method.data
            
            flash("Setup has been saved!")
            return redirect(url_for("setup.libraries"))
        
        return catalog.render(
            "setup.Authentication",
            form=form
        )
    
    return redirect(url_for("main.main"))

@setup_app.route("/libraries", methods=["GET", "POST"])
def libraries():
    form: LibrariesSetupForm = LibrariesSetupForm()

    if form.validate_on_submit():
        new_libraries = []
        
        # User(username=form.username.data)
        # new_user.set_password(form.password.data)
        # db.session.add(new_user)
        # db.session.commit()
        
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
        
        flash("Download has been configured!")
        return redirect(url_for("main.main"))
    
    return catalog.render(
        "setup.Download",
        form=form
    )