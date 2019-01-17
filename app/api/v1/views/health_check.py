import flask
import json
import flask_restful as restful


class HealthCheckView(restful.Resource):

    def get(self):
        return flask.make_response(
            json.dumps(
                {'message': 'The force is strong with this one.'}
            ), 200,
            {'Content-Type': 'application/json'}
        )
