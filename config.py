import os


class Config(object):
    # Used mostly as a CSRF token
    SECRET_KEY: str = os.getenv("SECRET_KEY") or "you-will-never-guess"
