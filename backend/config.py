import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite3')

class Production(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://docker:docker@db/flask_estoque"


config = dict(
    development=Development,
    production=Production,
)