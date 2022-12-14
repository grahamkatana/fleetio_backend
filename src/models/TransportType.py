from config.db import db
from datetime import datetime

class TransportType(db.Model):
    __tablename__ = 'transporttypes'
    id = db.Column(db.BigInteger, primary_key=True)
    type = db.Column(db.String(300), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow(),onupdate=datetime.utcnow())
  
    def __repr__(self):
        return '<TransportType %r>' % self.id
