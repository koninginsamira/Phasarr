from phasarr.variables import db_path

class Config:
    SECRET_KEY = "secret-key-goes-here"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + db_path