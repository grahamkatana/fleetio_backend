from functools import wraps
import jwt
from flask import request, abort, current_app
from models.User import User


def token_required(f):
    @wraps
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return {
                "message": "Authorization token is missing",
                "error": "Unauthorized"
            }, 401
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            user_id = data["id"]
            current_user = User
        except Exception as e:
            return {
                "message": "An error has occured",
                "error": str(e)
            }, 500
        return f(current_user, *args, ** kwargs)

    return decorated
