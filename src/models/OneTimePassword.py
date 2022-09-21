from email.policy import default
from config.db import db
from models.User import User
from datetime import datetime

class OneTimePassword(db.Model):
    __tablename__ = 'otps'
    
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    otp = db.Column(db.BigInteger,nullable=False)
    expires_in = db.Column(db.DateTime, nullable=False)
    is_valid = db.Column(db.Boolean,nullable=False,default=True)
    createdAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=True,default=datetime.utcnow(),onupdate=datetime.utcnow())
    user = db.relationship(
        User, backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<OneTimePassword %r>' % self.id
