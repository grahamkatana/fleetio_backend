
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controllers.auth_controller import register,current_user
main = Blueprint('auth_blueprint', __name__)


@main.route('/register', methods=["POST"])
def register_user():
    data = request.get_json()
    result = register(data)
    return result


@main.route('/login', methods=["POST"])
def login_user():
    pass

@main.route('/user', methods=["GET"])
@jwt_required()
def get_authenticated_user():
    user = current_user()
    return user

