from flask import jsonify
from models.User import User


def check_if_email_exists(email):
    user_exist = User.query.filter_by(email=email).first()
    if user_exist:
        return jsonify({
            "message": "This email already exist"
        }), 400
    else:
        return None
def check_if_cell_exists(cell):
    user_exist = User.query.filter_by(cell=cell).first()
    if user_exist:
        return jsonify({
            "message": "This cell number already exist"
        }), 400
    else:
        return None
def check_if_name_exists(name):
    user_exist = User.query.filter_by(name=name).first()
    if user_exist:
        return jsonify({
            "message": "This user name already exist"
        }), 400
    else:
        return None
