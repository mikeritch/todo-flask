import os, secrets

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Secret-Key-Placeholder'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False