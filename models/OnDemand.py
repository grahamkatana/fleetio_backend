from config.db import db
from models.Fleet import Fleet
from models.Company import Company

class OnDemand(db.Model):
    __tablename__ = 'ondemands'
    id = db.Column(db.BigInteger, primary_key=True)
    is_booked = db.Column(db.Boolean, nullable=False)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'))
    fleet_id = db.Column(db.BigInteger, db.ForeignKey('fleets.id'))
    company = db.relationship(Company, backref=db.backref('companies', lazy=True))
    fleet = db.relationship(Fleet, backref=db.backref('fleets', lazy=True))
    createdAt = db.Column(db.DateTime, nullable=True)
    updatedAt = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<OnDemand %r>' % self.name
