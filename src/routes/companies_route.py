
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from middleware.is_verified_middleware import is_verified
from controllers.company_controller import create, index
main = Blueprint('company_blueprint', __name__)


@main.route('/')
@jwt_required()
@is_verified
def get_companies(args):
    result= index()
    print(result)
    return result
   # try:
   #     result = []
   #     return jsonify({
   #         'data': 'Api is running'
   #     }), 200
   # except Exception as ex:
   #     return jsonify({
   #         'message': str(ex)
   #     }), 500


@main.route('/', methods=["POST"])
@jwt_required()
@is_verified
def create_new_company(args):
    result = create(request=request,
                    authenticated_email=args['email'], name=args['name'])
    print(result)
    return result
   # print(args['email'])
   # create(request=request,authenticated_email=args[])

   # print(request.form)
   # print(request.files)
   #  return jsonify({
   #     "message":result

   # }), 200

   # # user = current_user()
   # return user
