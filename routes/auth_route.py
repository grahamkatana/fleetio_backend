
from flask import Blueprint, jsonify, request
from controllers.auth_controller import register
main = Blueprint('auth_blueprint', __name__)


@main.route('/register', methods=["POST"])
def register_user():
    data = request.get_json()
    result = register(data)
    return result


@main.route('/login', methods=["POST"])
def login_user():
    pass
