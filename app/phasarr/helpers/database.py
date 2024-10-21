import os
import time
from flask_migrate import init, migrate, upgrade

from phasarr.variables import base_dir


def init_database(app, db):
    with app.app_context():
        from phasarr.models import user
        db.create_all()


def migrate_database(app):
    with app.app_context():
        # init(directory=os.path.join(base_dir, "migrations"))
        migrate(directory=os.path.join(base_dir, "migrations"), message=str(int(time.time())))
        upgrade(directory=os.path.join(base_dir, "migrations"))