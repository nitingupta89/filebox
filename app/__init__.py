'''
App Setup: Setting up facilities on flask application instance
that are required before starting the application
'''

import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    return app


flask_app = create_app()
from .api.v1 import urls # noqa
