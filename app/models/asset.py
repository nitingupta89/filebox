import datetime

from flask_security import current_user

from app import db, ma
from app.models.user import User
from app.api.services.s3 import delete_obj


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

    @classmethod
    def find_one(cls, **kwargs):
        return cls.query.filter_by(**kwargs).one()

    def delete(self):
        file_path = "users/{}/{}".format(current_user.id, self.file_name)
        delete_obj(file_path)
        db.session.delete(self)
        db.session.commit()


class AssetSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'file_name', 'file_type', 'file_url')
