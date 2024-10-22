from flask import redirect, url_for

from phasarr import app, db, http_auth
from phasarr.models.user import User

import sqlalchemy as sql


def login_required(func):
    def wrapper():
        user_exists = db.session.execute(sql.select(User)).first()

        if user_exists:
            return http_auth.login_required(func)
        else:
            return redirect(url_for('setup.setup'))
        
    return wrapper