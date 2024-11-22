import sqlalchemy as sql

from flask_login import login_user

from phasarr import db, login, http_auth
from phasarr.models.user import User


@http_auth.verify_password
def verify_password(username, password):
    user = db.session.scalar(sql.select(User).where(User.username == username))

    if user and user.check_password(password):
        login_user(user)
        return user.username

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))