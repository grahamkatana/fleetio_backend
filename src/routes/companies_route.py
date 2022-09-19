
from flask import Blueprint, jsonify
from config import db
main = Blueprint('company_blueprint', __name__)


@main.route('/')
def get_companies():
    try:
        result = []
        return jsonify({
            'data': 'Api is running'
        }), 200
    except Exception as ex:
        return jsonify({
            'message': str(ex)
        }), 500
