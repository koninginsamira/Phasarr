from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from phasarr import http_auth


auth_app = Blueprint('auth', __name__)

users = {
    "john": generate_password_hash("hello", "scrypt"),
    "susan": generate_password_hash("bye", "scrypt")
}


@http_auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username