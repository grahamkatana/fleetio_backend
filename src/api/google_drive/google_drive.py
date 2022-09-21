from pathlib import Path
from flask import current_app
from create_google_service import create_service
CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]
PARENT_FOLDER_ID = current_app.config['BACKUP_DRIVE']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# print("test")