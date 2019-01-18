import os

from flask.config import Config

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(Config):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['APP_SECRET_KEY']

    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ['PG_DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Google oauth config
    CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
    CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']
    REDIRECT_URI = os.environ['GOOGLE_REDIRECT_URI']
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class StagingConfig(BaseConfig):
    DEBUG = True


config = {
    "development": DevelopmentConfig,
    "staging": StagingConfig,
    "default": DevelopmentConfig
}
