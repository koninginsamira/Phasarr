import sqlalchemy as sql

from flask_login import current_user
from flask import Blueprint, flash, redirect, url_for

from phasarr import db, config, catalog
from phasarr.models.user import User
from phasarr.forms.setup import SetupForm

setup_app = Blueprint("setup", __name__)


@setup_app.route("/", methods=["GET", "POST"])
def setup():
    user_exists = db.session.execute(sql.select(User)).first()

    if not user_exists:
        # if current_user.is_authenticated:
        #     return redirect(url_for("main.main"))
        
        form: SetupForm = SetupForm()

        if form.validate_on_submit():
            new_user = User(username=form.username.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()

            config.authentication.method = form.auth_method.data
            
            flash("Setup has been saved!")
            return redirect(url_for("main.main"))
        
        return catalog.render(
            "setup.Setup",
            title="Setup",
            form=form
        )
    
    return redirect(url_for("main.main"))