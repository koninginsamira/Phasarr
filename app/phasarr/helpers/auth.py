import sqlalchemy as sql

from functools import wraps
from flask import redirect, url_for

from phasarr import db, http_auth
from phasarr.models.user import User


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_exists = db.session.execute(sql.select(User)).first()

        if user_exists:
            return http_auth.login_required(func)(*args, **kwargs)
        else:
            return redirect(url_for('setup.setup'))
        
    return wrapper