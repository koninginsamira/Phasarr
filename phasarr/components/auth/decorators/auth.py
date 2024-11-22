import flask_login

from functools import wraps
from flask_login import current_user

from phasarr import http_auth, config, db
from phasarr.components.utilities.helpers.sql import get_row_count_from
from phasarr.models.user import User


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_mode = config.authentication.method

        if not current_user.is_authenticated:
            match auth_mode:
                case "prompt":
                    return http_auth.login_required(func)(*args, **kwargs)
                case "form":
                    return flask_login.login_required(func)(*args, **kwargs)
                case _:
                    raise ValueError(
                        "Authentication mode '" + auth_mode + "' is not supported. \
                            Remove the config file to generate a correct one.")
        else:
            return func(*args, **kwargs)
        
    return wrapper


def login_required_if_user_exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_exists = get_row_count_from(db, User) > 0

        if user_exists:
            return login_required(func)(*args, **kwargs)
        else:
            return func(*args, **kwargs)
        
    return wrapper