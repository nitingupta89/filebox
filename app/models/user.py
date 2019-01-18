import datetime

from app import db, google_bp
from sqlalchemy.dialects.postgresql import JSON
from flask_login import current_user
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<id {}>'.format(self.id)


class OAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = 'oauth_info'

    token = db.Column(db.String(100), nullable=True)
    provider_user_id = db.Column(db.Integer)
    provider = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)


google_bp.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user)
