import random
from flask import jsonify
from config import db
from utils.send_email import send_email
from config.bcrypt import bcrypt
from models.User import User
from models.OneTimePassword import OneTimePassword
from datetime import date, datetime
from utils.validators import check_if_cell_exists, check_if_email_exists, check_if_name_exists
from utils.database_operations import save_record
from utils.jwt_helper import encode_jwt, get_auth_user
from datetime import timedelta
from datetime import timezone
from sqlalchemy.sql import text
from utils.messages import message

# ----------------------------------------------------------------------------
# Register a user
# ----------------------------------------------------------------------------


def register(request):
    hash_password = bcrypt.generate_password_hash(request['password'])
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
        record = save_record(user, db)
        user_id = record[0]['data']
        now = datetime.now(timezone.utc)
        generated_otp = random.randint(10000, 99999)
        target_timestamp = datetime.timestamp(now + timedelta(hours=24))
        otp_data = OneTimePassword(user_id=user_id, otp=generated_otp,
                                   expires_in=datetime.fromtimestamp(target_timestamp), is_valid=True)
        save_record(otp_data, db)
        identity = {'name': request['name'], 'user_id': user_id, 'joined': datetime.now(), 'email': request['email'], 'role': request['role'], 'cell': request['cell'], 'status': 'inactive', "email_verified_at": "",
                    }
        token = encode_jwt(identity)
        is_sent = send_email(
            recipients=request['email'], message=f"Hello {request['name']}! Thank you for joining FleetIO. Your OTP is {generated_otp}. You will need this OTP to verify your email. Your OTP is valid for 24 hours from now.", subject="Welcome to FleetIO", sender="app@fleetio.com")
        return jsonify({
            "data": identity,
            "jwt_token": token
        }), 201
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500

# ----------------------------------------------------------------------------
# Login a user
# ----------------------------------------------------------------------------


def login(request):

    check_email = User.query.filter_by(email=request['email']).first()
    if check_email:
        email = check_email.email
        password = check_email.password
        plain_password = request['password']
        check_password = bcrypt.check_password_hash(password, plain_password)
        if not check_password:
            return message("Invalid credentials given", 401)
        if check_password and email:
            identity = {'name': check_email.name, 'user_id': check_email.id, 'joined': check_email.createdAt, 'email': request['email'], 'role': check_email.role, 'cell': check_email.cell, 'status': check_email.status, "email_verified_at": check_email.email_verified_at,
                        }
            token = encode_jwt(identity)
            return jsonify({
                "data": identity,
                "jwt_token": token
            }), 200
    else:
        return message("The account does not exist", 404)


# ----------------------------------------------------------------------------
# Get authenticated user
# ----------------------------------------------------------------------------


def current_user():
    current_user = get_auth_user()
    return jsonify(current_user), 200


# ----------------------------------------------------------------------------
# Verify email
# ----------------------------------------------------------------------------

def verify(otp):
    now = datetime.now()
    current_user = get_auth_user()
    user = User.query.filter_by(email=current_user['email']).first()
    get_otp = OneTimePassword.query.filter_by(
        user_id=user.id).order_by(text("id desc")).first()
    if user.email_verified_at:
        return message("This account has been verified", 409)
    elif not int(get_otp.otp) == int(otp):
        return message("The given otp does not match", 404)

    elif get_otp.expires_in < now:
        return message("This otp has expired", 400)
    elif not get_otp.is_valid:
        return message("This otp is not valid", 400)

    user.email_verified_at = now
    get_otp.is_valid = False
    db.db.session.commit()
    return jsonify(current_user), 200


def resend_verification(request):
    print(request)

# ----------------------------------------------------------------------------
# Reset password
# ----------------------------------------------------------------------------


def reset(email):
    check_email = User.query.filter_by(email=email).first()
    if check_email:
        email = check_email.email
        get_otp = OneTimePassword.query.filter_by(
            user_id=check_email.id).order_by(text("id desc")).first()
        if get_otp:
            get_otp.is_valid = False
            db.db.session.commit()
        generated_otp = random.randint(10000, 99999)
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(hours=24))
        otp_data = OneTimePassword(user_id=check_email.id, otp=generated_otp,
                                   expires_in=datetime.fromtimestamp(target_timestamp), is_valid=True)
        save_record(otp_data, db)

        is_sent = send_email(
            recipients=check_email.email, message=f"Greetings {check_email.name}, We have received a password reset request. Your OTP to reset the password is {generated_otp}. If you did not request the password reset, no further action is required. Your OTP is valid for 24 hours from now. If this is a suspected breach please contact us.", subject="Reset password FleetIO", sender="app@fleetio.com")
        return message("Please check your email.", 201)


def save_new_password(request):
    print(request)
