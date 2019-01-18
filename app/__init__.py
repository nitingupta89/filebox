'''
App Setup: Setting up facilities on flask application instance
that are required before starting the application
'''

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dance.contrib.google import make_google_blueprint
from flask_login import LoginManager

from app.config import config
from app.blueprint import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config[os.environ["APP_ENV"]])
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app


flask_app = create_app()
login_manager = LoginManager()
login_manager.init_app(flask_app)
db = SQLAlchemy(flask_app)

google_bp = make_google_blueprint(
    client_id=os.environ['GOOGLE_CLIENT_ID'],
    client_secret=os.environ['GOOGLE_CLIENT_SECRET'],
    scope=[
        "profile", "email"
    ]
)

flask_app.register_blueprint(google_bp, url_prefix="/login")


from .api.v1 import urls # noqa

from .views import file_upload # noqa
from .views import login # noqa
