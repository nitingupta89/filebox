import flask
import json
from flask import request
import flask_restful as restful


class AssetsView(restful.Resource):

    def post(self):
        import pdb; pdb.set_trace()

        Asset.create(file_name=file_name, file_type=file_type,
                      file_url=file_url, user=current_user)


        return flask.make_response(
            json.dumps(
                {'message': 'File uploaded successfully'}
            ), 200,
            {'Content-Type': 'application/json'}
        )
