import flask
import json
from flask import request
from flask_security import current_user
import flask_restful as restful

from app.models.asset import Asset


class AssetsView(restful.Resource):

    def post(self):
        kwargs = request.json
        kwargs['user'] = current_user
        Asset.create(**kwargs)


        return flask.make_response(
            json.dumps(
                {'message': 'File uploaded successfully'}
            ), 200,
            {'Content-Type': 'application/json'}
        )
