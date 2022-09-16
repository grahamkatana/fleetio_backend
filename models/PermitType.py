from config.db import db
from models.Company import Company


class PermitType(db.Model):
    __tablename__ = 'permittypes'
    id = db.Column(db.BigInteger, primary_key=True)
    is_local = db.Column(db.Boolean, nullable=False)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'))
    regions = db.Column(db.String(300), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=True)
    updatedAt = db.Column(db.DateTime, nullable=True)
    company = db.relationship(
        Company, backref=db.backref('companies', lazy=True))

    def __repr__(self):
        return '<PermitType %r>' % self.id
