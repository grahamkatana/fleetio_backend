from config.db import db
from models.Company import Company
from datetime import datetime


class TransportType(db.Model):
    __tablename__ = 'transporttypes'
    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'))
    type = db.Column(db.String(300), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow(),onupdate=datetime.utcnow())
    company = db.relationship(
        Company, backref=db.backref('companies', lazy=True))

    def __repr__(self):
        return '<TransportType %r>' % self.id
