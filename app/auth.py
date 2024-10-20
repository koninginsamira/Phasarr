from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


auth_app = Blueprint('auth', __name__)
auth = HTTPBasicAuth()


users = {
    "john": generate_password_hash("hello", "scrypt"),
    "susan": generate_password_hash("bye", "scrypt")
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username