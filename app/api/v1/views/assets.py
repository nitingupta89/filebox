import flask
import json
from flask import request
from flask_security import current_user
import flask_restful as restful
from sqlalchemy.orm.exc import NoResultFound

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
        try:
            asset = Asset.find_one(id=int(asset_id), user_id=current_user.id)
            asset.delete()
            return flask.make_response(
                json.dumps(
                    {'message': 'File deleted successfully'}
                ), 200,
                {'Content-Type': 'application/json'}
            )
        except NoResultFound:
            return flask.make_response(
                json.dumps(
                    {'message': 'Access Denied'}
                ), 403,
                {'Content-Type': 'application/json'}
            )

