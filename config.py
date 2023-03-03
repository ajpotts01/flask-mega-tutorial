import os

basedir = os.path.abspath(os.path.dirname(__file__))  # ?


class Config(object):
    # Used mostly as a CSRF token
    SECRET_KEY: str = os.getenv("SECRET_KEY") or "you-will-never-guess"

    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
