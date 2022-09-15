
from flask import Blueprint, jsonify
from config import db

# from models.BundleHistory import Bundle
main = Blueprint('company_blueprint', __name__)




@main.route('/')
def get_companies():
    # response = load_companies()
    # print(response)
    # user = Bundle(username="graham", email="graykatanakenny@gmail.com")
    # db.db.session.add(user)
    # db.db.session.commit()
    # return response
    try:
        result = []
        return jsonify({
            'data':'Api is running'
        }), 200
    except Exception as ex:
        return jsonify({
            'message': str(ex)
        }), 500
