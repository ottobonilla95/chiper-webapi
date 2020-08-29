from db import db
from datetime import datetime

class AuditoryLogModel(db.Model):

    __tablename__ = 'auditory_log'
    id = db.Column(db.Integer, primary_key=True)
    proccess = db.Column(db.String(40))
    module = db.Column(db.String(40))
    method = db.Column(db.String(40))
    message = db.Column(db.String(500))
    date = db.Column(db.DateTime, default=datetime.utcnow)
   
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
