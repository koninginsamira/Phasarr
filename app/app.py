import logging
import os
import time
from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if os.environ["FLASK_ENV"] == "development":
    import debugpy

    debugpy.listen(("0.0.0.0", int(os.environ["DEBUG_PORT"])))

    app.logger.debug("Waiting for client to attach...")
    debugpy.wait_for_client()
    app.logger.debug("Client has attached!")

# login_manager = LoginManager()

# app.secret_key = print(os.environ["FLASK_SECRET"])
# app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.environ['CONFIGPATH']}/database.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# login_manager.init_app(app)
# db.init_app(app)
# migrate.init_app(app, db)

users = {
    "john": generate_password_hash("hello", "scrypt"),
    "susan": generate_password_hash("bye", "scrypt")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    
@app.route("/setup")
def setup():
    return "setup"

@app.route("/")
@auth.login_required
def main():
    return render_template("index.html")

@app.route("/api/time")
def get_current_time():
    return {"time": time.time()}