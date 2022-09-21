'''
+----------------------------------------------------------------------------
| Description
+----------------------------------------------------------------------------
| Simple helper to send messages to client based on error codes and message
+----------------------------------------------------------------------------
'''
from flask import jsonify
def message(message,code):
    return jsonify({"message":message}),code