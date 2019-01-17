from flask import Blueprint
from flask_restful import Api

# Create a Flask blueprint
api_bp = Blueprint('v1', __name__)

# Register the API (flask-restful) with v1 blueprint
api = Api(api_bp)
