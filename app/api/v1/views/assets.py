import flask
import json
from flask import request
from flask_security import current_user
import flask_restful as restful

from app.models.asset import Asset, AssetSchema


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

    def get(self):
        asset_schema = AssetSchema(many=True)
        all_assets = Asset.query.filter_by(user_id=current_user.id).all()
        return asset_schema.jsonify(all_assets)


class AssetView(restful.Resource):

    def delete(self, asset_id):
        asset_schema = AssetSchema(many=True)
        all_assets = Asset.query.filter_by(user_id=current_user.id).all()
        return asset_schema.jsonify(all_assets)
