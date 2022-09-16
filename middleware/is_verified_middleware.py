from functools import wraps
from utils.jwt_helper import get_auth_user
# import jwt
# from flask import request, abort, current_app
# from models.User import User


def is_verified(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        is_verified = False
        current_user = get_auth_user()
        status = current_user['status']
        verified_at = current_user['email_verified_at']
        if not verified_at and status=="inactive":
            return {
                'message':'Please verify your account',
            },401
        else:
            is_verified=True

        # return f(is_verified, *args, ** kwargs)
        # if "Authorization" in request.headers:
        #     token = request.headers['Authorization'].split(" ")[1]
        # if not token:
        #     return {
        #         "message": "Authorization token is missing",
        #         "error": "Unauthorized"
        #     }, 401
        # try:
        #     data = jwt.decode(
        #         token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        #     user_id = data["id"]
        #     current_user = User
        # except Exception as e:
        #     return {
        #         "message": "An error has occured",
        #         "error": str(e)
        #     }, 500
        return f(current_user, *args, ** kwargs)

    return decorated
