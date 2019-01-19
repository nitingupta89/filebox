import datetime

from app import db, ma
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

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'file_name'  : self.file_name,
           'file_type'  : self.file_type,
           'created_at' : self.dump_datetime(self.created_at),
       }

    def dump_datetime(value):
        """Deserialize datetime object into string form for JSON processing."""
        if value is None:
            return None
        return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class AssetSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'file_name', 'file_type', 'file_url')
