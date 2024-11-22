import sqlalchemy as sql

from flask import redirect, request, url_for, current_app as app

from phasarr import db, config
from phasarr.setup import setup_app, stages
from phasarr.models.user import User
from phasarr.components.utilities.helpers.list import find_index
from phasarr.components.utilities.helpers.sql import get_row_count_from


@setup_app.before_request
def check_stage():
        stage_endpoint = request.endpoint.split(".")[-1]
        stage_exists = find_index(list(stages), stage_endpoint)
        current_stage = config.setup.stage
        request_stage = stage_exists

        if stage_exists:
            stage_is_blocked = request_stage > current_stage

            if stage_is_blocked:
                return redirect(url_for("setup.setup"))
        else:
            setup_is_done = current_stage > len(stages)

            if setup_is_done:
                return redirect(url_for("main.main"))


@setup_app.before_request
def check_user_count():
    user_count = get_row_count_from(db, User)

    if user_count > 1:
        app.logger.warning(
            "Setup cannot be started with more than one user.")
        
        redirect(url_for("main.main"))


@setup_app.before_request
def check_existing_data():
    user_exists = bool(db.session.execute(sql.select(User)).scalar_one_or_none())
    auth_mode_is_set = bool(config.authentication.method)

    stages["authentication"]["skippable"] = 1 if user_exists and auth_mode_is_set else 0