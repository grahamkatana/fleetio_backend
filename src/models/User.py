from config.db import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    email_verified_at = db.Column(db.DateTime, nullable=True)
    password = db.Column(db.String(120), unique=True, nullable=False)
    cell = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    remember_token = db.Column(db.String(120), nullable=True)
    access_token = db.Column(db.String(120), nullable=True)
    status = db.Column(db.String(120), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow(),onupdate=datetime.utcnow())

    def __repr__(self):
        return '<User %r>' % self.id
