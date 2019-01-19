import json
import flask
from flask import request
import json
import flask_restful as restful

from app.api.services.s3 import generate_presigned_post, generate_presigned_url
from .utils import get_s3_url


class S3View(restful.Resource):
    def get(self):
        url_type = request.args.get('url_type')
        presigned_post = {}
        file_url = None

        if url_type == "presigned_post":
            presigned_post, file_url = self.get_presigned_post_data()
        else:
            file_url = self.get_presigned_url()

        # Return the data to the client

        return flask.make_response(
            json.dumps({
                'data': presigned_post,
                'url': file_url
            }), 200,
            {'Content-Type': 'application/json'}
        )

    def get_presigned_post_data(self):
        # Load required data from the request
        file_name = request.args.get('file_name')
        file_type = request.args.get('file_type')

        # Generate and return the presigned URL
        presigned_post = generate_presigned_post(
            file_name,
            file_type
        )

        file_url = get_s3_url(file_name)
        return presigned_post, file_url

    def get_presigned_url(self):
        file_name = request.args.get('file_name')
        return generate_presigned_url(file_name)
