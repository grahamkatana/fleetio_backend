from flask import jsonify
from config import db
from utils.send_email import send_email
from config.bcrypt import bcrypt
from models.User import User
from datetime import datetime
from utils.validators import check_if_email_exists
from utils.database_operations import save_record


def register(request):
    hash_password = bcrypt.generate_password_hash(request['password'])
    # check_password = bcrypt.check_password_hash(hash_password,'hunter2')
    # print(hash_password)
    # print(check_password)
    try:
        check_email = check_if_email_exists(request['email'])
        if check_email:
            return check_email
        user = User(name=request['name'], email=request['email'], password=hash_password, cell=request['cell'],
                    role=request['role'], status='inactive', createdAt=datetime.now(),updatedAt=datetime.now())
        save_record(user, db)
        return jsonify(request), 201
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500


def login_user(request):
    print(request)


def verify_account(request):
    print(request)


def resend_verification(request):
    print(request)


def reset_password(request):
    print(request)


def save_new_password(request):
    print(request)
