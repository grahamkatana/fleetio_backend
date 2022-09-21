'''
+----------------------------------------------------------------------------
| Description
+----------------------------------------------------------------------------
| Get the current authenticated user and encode a jwt token
| Encode the information to be encoded in the jwt for identity 
| Get the information of the current authenticated user
+----------------------------------------------------------------------------
'''

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity

def encode_jwt(user):
      access_token = create_access_token(identity=user)
      return access_token

def get_auth_user():
      current_user = get_jwt_identity()
      return current_user