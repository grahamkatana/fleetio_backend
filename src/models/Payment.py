from config.db import db
from datetime import datetime
from models.Company import Company

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.BigInteger, primary_key=True)
    reference = db.Column(db.String(300), nullable=False)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'))
    company = db.relationship(
        Company, backref=db.backref('companies', lazy=True))
    createdAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow(),onupdate=datetime.utcnow())
  
    def __repr__(self):
        return '<TransportType %r>' % self.id
