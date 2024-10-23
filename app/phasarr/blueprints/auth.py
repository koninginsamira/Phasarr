import sqlalchemy as sql
from flask import Blueprint

from phasarr import http_auth, db
from phasarr.models.user import User


auth_app = Blueprint("auth", __name__)


@http_auth.verify_password
def verify_password(username, password):
    user = db.session.scalar(sql.select(User).where(User.username == username))

    if user and user.check_password(password):
        return user.username