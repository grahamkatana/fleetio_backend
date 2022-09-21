'''
+----------------------------------------------------------------------------
| Description
+----------------------------------------------------------------------------
| Simple helper to send messages to client based on error codes and message
+----------------------------------------------------------------------------
'''
from flask import jsonify
from datetime import datetime
def message(message,code):
    return jsonify({"message":message}),code

def greet_get_time():
    now = datetime.now()
    print(now)
    if now.hour<12:
        return "Hello, good morning"
    elif now.hour<16:
        return "A great afternoon"
    elif now.hour<19:
        return "Good evening"
    else:
        return "Hie"
    
    pass