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

from utils.messages import message
from utils.rand_string_generator import get_random_string
from flask import current_app
from werkzeug.utils import secure_filename
import os
from datetime import date

def upload_client_files(request,destination,client_message,error_message):
    file = request.files['file']
    if file:
        filename = secure_filename(f"{date.today()}_{get_random_string(25)}_{file.filename}")
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER']+destination, filename))
        return filename
    else:
        return "error"
