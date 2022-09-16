from email.policy import default
from config.db import db
from models.User import User
from datetime import datetime

# from datetime import timedelta
# from datetime import timezone
# exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
#         if target_timestamp > exp_timestamp:
# now = datetime.now(timezone.utc)
#     target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
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
