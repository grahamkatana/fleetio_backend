from config.db import db

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(80), nullable=True)
    tags = db.Column(db.String(300), nullable=True)
    active = db.Column(db.Boolean, nullable=False)
    industry_type = db.Column(db.String(80), nullable=True)
    latitude = db.Column(db.String(80), nullable=True)
    longitude = db.Column(db.String(80), nullable=True)
    logo = db.Column(db.String(200), nullable=True)
    createdAt = db.Column(db.DateTime, nullable=True)
    updatedAt = db.Column(db.DateTime, nullable=True)
    def __repr__(self):
        return '<Company %r>' % self.name
