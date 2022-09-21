'''
+----------------------------------------------------------------------------
| Description
+----------------------------------------------------------------------------
| Validate your request first before you proceed to save the file in your
| storage. The function take 3 args 
| request:
| client_message: the success message you want to be shown on success 
| error_message: the error message you want to be shown on error
+----------------------------------------------------------------------------
'''

from messages import message
from flask import current_app
from werkzeug.utils import secure_filename
import os
import time

def upload_client_files(request,client_message,error_message):
    file = request.files['file']
    if file:
        filename = secure_filename(f"{time.time()}_{file.filename}")
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return message(client_message,201)
    else:
        return message(error_message,400)
