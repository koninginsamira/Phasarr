import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from phasarr.helpers.file import remove_protocol


is_upgrade = "db" in sys.argv and "upgrade" in sys.argv

def init_database(app: Flask, db: SQLAlchemy):
    with app.app_context():
        db_uri: str = app.config["SQLALCHEMY_DATABASE_URI"]
        db_path = remove_protocol(db_uri)
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        import phasarr.models
        db.create_all()