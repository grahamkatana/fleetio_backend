from functools import wraps
from utils.jwt_helper import get_auth_user
from models.User import User

# import jwt
# from flask import request, abort, current_app
# from models.User import User


def is_verified(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        current_user = get_auth_user()
        user = User.query.filter_by(email=current_user['email']).first()
        verified_at = user.email_verified_at
        if not verified_at:
            return {
                'message':'Please verify your account',
            },401

        return f(current_user, *args, ** kwargs)

    return decorated
