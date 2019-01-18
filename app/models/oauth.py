from flask_security import current_user
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend

from app import db, google_bp
from app.models.user import User


class OAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = 'oauth_info'

    provider_user_id = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)


google_bp.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user,
                                      user_required=False)
