from flask_login import current_user, login_user
from flask import flash, redirect, request, url_for, current_app as app

from phasarr import db, config, catalog
from phasarr.setup import setup_app, stages
from phasarr.setup.forms import AuthSetupForm
from phasarr.components.auth.decorators.auth import login_required_if_user_exists
from phasarr.models.user import User


@setup_app.route("/authentication", methods=["GET", "POST"])
@login_required_if_user_exists
def authentication():
    user = current_user
    auth_mode = config.authentication.method
    user_exists = current_user.is_authenticated
    auth_mode_is_set = bool(auth_mode)

    form: AuthSetupForm = AuthSetupForm(edit_user=user_exists, edit_auth_mode=auth_mode_is_set)

    match request.method:
        case "GET":
            if user_exists:
                form.previous_username.data = current_user.username
                form.username.data = current_user.username

            if auth_mode_is_set:
                form.auth_method.data = auth_mode

        case "POST":
            if form.validate_on_submit():
                new_username = form.username.data
                new_password = form.password.data
                new_auth_mode = form.auth_method.data

                if user_exists:
                    if new_username:
                        user.username = new_username
                    if new_password:
                        user.set_password(new_password)
                    if new_username or new_password:
                        pass
                else:
                    user = User(username=new_username)
                    user.set_password(new_password)
                    db.session.add(user)
                db.session.commit()

                config.authentication.method = new_auth_mode
                config.setup.stage = 1

                if not login_user(user):
                    app.logger.error("New user could not be logged in.")
                
                flash("Authentication has been configured!")
                return redirect(url_for("setup.libraries"))
    
    return catalog.render(
        "setup.Authentication",
        current_stage="authentication",
        stages=stages,
        form=form
    )