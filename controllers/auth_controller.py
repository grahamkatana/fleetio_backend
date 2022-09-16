from flask import jsonify
from config import db
from utils.send_email import send_email
from config.bcrypt import bcrypt
from models.User import User
from datetime import datetime
from utils.validators import check_if_cell_exists, check_if_email_exists, check_if_name_exists
from utils.database_operations import save_record
from utils.jwt_helper import encode_jwt,get_auth_user

# ----------------------------------------------------------------------------
# Register a user
# ----------------------------------------------------------------------------
def register(request):
    hash_password = bcrypt.generate_password_hash(request['password'])
    # check_password = bcrypt.check_password_hash(hash_password,'hunter2')
    # print(hash_password)
    # print(check_password)
    try:
        check_email = check_if_email_exists(request['email'])
        check_cell = check_if_cell_exists(request['cell'])
        check_name = check_if_name_exists(request['name'])
        if check_email:
            return check_email
        if check_cell:
            return check_cell
        if check_name:
            return check_name
        user = User(name=request['name'], email=request['email'], password=hash_password, cell=request['cell'],
                    role=request['role'], status='inactive', createdAt=datetime.now(), updatedAt=datetime.now())
        save_record(user, db)
        identity = {'name': request['name'], 'email': request['email'], 'role': request['role'], 'cell': request['cell'], 'status': 'inactive', "email_verified_at": "",
                    }
        token = encode_jwt(identity)
        return jsonify({
            "data": request,
            "jwt_token": token
        }), 201
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500

# ----------------------------------------------------------------------------
# Login a user
# ----------------------------------------------------------------------------
def login_user(request):
    print(request)

# ----------------------------------------------------------------------------
# Get authenticated user
# ----------------------------------------------------------------------------
def current_user():
    current_user = get_auth_user()
    return jsonify(current_user), 200


def verify_account(request):
    print(request)


def resend_verification(request):
    print(request)


def reset_password(request):
    print(request)


def save_new_password(request):
    print(request)
