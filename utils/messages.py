from flask import jsonify
def message(message,code):
    return jsonify({"message":message}),code