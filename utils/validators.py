import json
from flask import jsonify
from models.User import User


def check_if_email_exists(email):
    user_exist = User.query.filter_by(email=email).first()
    if user_exist:
        return jsonify({
            "message": "This email already exist"
        }), 401
    else:
        return None
