import datetime

from app import db
from app.models.user import User


class Asset(db.Model):
    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(), unique=True, nullable=False)
    file_type = db.Column(db.String(), nullable=True)
    file_url = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<id {}>'.format(self.id)

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
