
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from middleware.is_verified_middleware import is_verified
from controllers.auth_controller import register,save_new_password, reset,current_user, login,verify
main = Blueprint('auth_blueprint', __name__)


@main.route('/register', methods=["POST"])
def register_user():
    data = request.get_json()
    result = register(data)
    return result


@main.route('/login', methods=["POST"])
def login_user():
    data = request.get_json()
    result = login(data)
    return result


@main.route('/user', methods=["GET"])
@jwt_required()
@is_verified
def get_authenticated_user(args):
    user = current_user()
    return user

@main.route('/verify/<otp>', methods=["POST"])
@jwt_required()
def verify_user(otp):
    result = verify(otp)
    return result

@main.route('/reset/<email>', methods=["POST"])
def reset_password(email):
    result = reset(email)
    return result

@main.route('/update/<otp>', methods=["POST"])
def update_password(otp):
    data = request.get_json()
    result = save_new_password(data,otp)
    return result