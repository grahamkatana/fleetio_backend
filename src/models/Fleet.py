from config.db import db
from models.Company import Company
from models.PermitType import PermitType
from models.TransportType import TransportType
from datetime import datetime


class Fleet(db.Model):
    __tablename__ = 'fleets'
    id = db.Column(db.BigInteger, primary_key=True)
    is_booked = db.Column(db.Boolean, nullable=False)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'))
    permit_type_id = db.Column(db.BigInteger, db.ForeignKey('permittypes.id'))
    transport_type_id = db.Column(
        db.BigInteger, db.ForeignKey('transporttypes.id'))
    make = db.Column(db.String(80), nullable=False)
    year = db.Column(db.BigInteger, nullable=False)
    registration_number = db.Column(db.String(80), nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False)
    permit_type = db.Column(db.String(300), nullable=False)
    mileage = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(300), nullable=False)
    company = db.relationship(
        Company, backref=db.backref('companies', lazy=True))
    permit_type = db.relationship(
        PermitType, backref=db.backref('permittypes', lazy=True))
    tranport_type = db.relationship(
        TransportType, backref=db.backref('transporttypes', lazy=True))
    createdAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow(),onupdate=datetime.utcnow())

    def __repr__(self):
        return '<Fleet %r>' % self.id
