'''
App Setup: Setting up facilities on flask application instance
that are required before starting the application
'''

import os

from flask import Flask

from app.config import AppConfig
from app.blueprint import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app


flask_app = create_app()
from .api.v1 import urls # noqa
