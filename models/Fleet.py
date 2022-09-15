from config.db import db
from models.Company import Company

class Fleet(db.Model):
    __tablename__ = 'fleets'
    id = db.Column(db.BigInteger, primary_key=True)
    is_booked = db.Column(db.Boolean, nullable=False)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'))
    make = db.Column(db.String(80),nullable=False)
    year = db.Column(db.BigInteger, nullable=False)
    registration_number = db.Column(db.String(80), nullable=False)
    date_registered = db.Column(db.DateTime,nullable=False)
    mileage = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(80), nullable=False)
    company = db.relationship(Company, backref=db.backref('companies', lazy=True))
    createdAt = db.Column(db.DateTime, nullable=True)
    updatedAt = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<Fleet %r>' % self.id
