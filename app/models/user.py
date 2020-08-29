from db import db
from datetime import datetime

class UserModel(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(100))
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def find_by_username(cls, username) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, _email) -> "UserModel":
        return cls.query.filter_by(email=_email).first()

    @classmethod
    def find_by_username_or_email(cls, _username_email) -> "UserModel":
        return cls.query.filter((cls.username == _username_email)|(cls.email == _username_email)).first()

    @classmethod
    def find_by_id(cls, id) -> "UserModel":
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
