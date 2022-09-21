from email.policy import default
from config.db import db
from models.Fleet import Fleet
from models.Company import Company
from datetime import datetime


class OnDemand(db.Model):
    __tablename__ = 'ondemands'
    id = db.Column(db.BigInteger, primary_key=True)
    is_booked = db.Column(db.Boolean, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False,default=False)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'))
    expires_at = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    fleet_id = db.Column(db.BigInteger, db.ForeignKey('fleets.id'))
    company = db.relationship(
        Company, backref=db.backref('companies', lazy=True))
    fleet = db.relationship(Fleet, backref=db.backref('fleets', lazy=True))
    createdAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow(),onupdate=datetime.utcnow())

    def __repr__(self):
        return '<OnDemand %r>' % self.name
