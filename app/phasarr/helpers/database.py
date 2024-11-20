import time

from flask import Flask
from flask_migrate import migrate, upgrade


def init_database(app: Flask, db):
    with app.app_context():
        import phasarr.models
        db.create_all()


def migrate_database(app: Flask, dir: str):
    with app.app_context():
        migrate(directory=dir, message=str(int(time.time())))
        upgrade(directory=dir)