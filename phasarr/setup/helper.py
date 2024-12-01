import sqlalchemy as sql

from flask import redirect, request, url_for, current_app as app

from phasarr import db, config
from phasarr.components.utilities.helpers.dictionary import find_item
from phasarr.setup import setup_app, stages
from phasarr.models.user import User
from phasarr.components.utilities.helpers.sql import get_row_count_from


@setup_app.before_request
def check_user_count():
    user_count = get_row_count_from(db, User)

    if user_count > 1:
        app.logger.warning(
            "Setup cannot be started with more than one user.")
        
        redirect(url_for("main.main"))


@setup_app.before_request
def check_existing_data():
    # Check Authentication stage
    user_exists = bool(db.session.execute(sql.select(User)).scalar_one_or_none())
    auth_mode_is_set = bool(config.authentication.method)

    stages["authentication"]["skippable"] = 1 if user_exists and auth_mode_is_set else 0

    # Check Libraries stage
    auth_stage_is_skippable = stages["authentication"]["skippable"]

    stages["libraries"]["skippable"] = 1 if auth_stage_is_skippable else 0


@setup_app.before_request
def check_stage():
        current_stage = config.setup.stage
        setup_is_done = current_stage >= len(stages)

        if setup_is_done:
            return redirect(url_for("main.main"))
        
        stage_endpoint = request.endpoint.split(".")[-1]
        stage_exists = stage_endpoint in stages

        if stage_exists:
            request_stage = stages[stage_endpoint]["stage"]
            is_future_stage = request_stage > current_stage

            if is_future_stage:
                for stage in range(current_stage, request_stage):
                    is_skippable = find_item(stages, ("stage", stage))["skippable"]

                    if not is_skippable:
                        return redirect(url_for("setup.setup"))