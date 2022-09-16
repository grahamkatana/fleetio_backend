from config.db import db
from models.Company import Company


class TransportType(db.Model):
    __tablename__ = 'transporttypes'
    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'))
    type = db.Column(db.String(300), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=True)
    updatedAt = db.Column(db.DateTime, nullable=True)
    company = db.relationship(
        Company, backref=db.backref('companies', lazy=True))

    def __repr__(self):
        return '<TransportType %r>' % self.id
