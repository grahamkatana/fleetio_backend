import os
from datetime import timedelta
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from routes import auth_route, companies_route
from config.db import db, migrate
from config.mail import mail
from config.bcrypt import bcrypt
from config.jwt import jwt
from utils.database_connection import get_connection_string

# app declaration
app = Flask(__name__)
CORS(app)
load_dotenv()

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# secret key
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2160)

# mail configuration
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] =bool(os.environ.get('MAIL_USE_TLS'))
app.config['MAIL_USE_SSL'] = bool(os.environ.get('MAIL_USE_SSL'))


# initialize the database
db.init_app(app)
migrate.init_app(app, db)
mail.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# app routes
app.register_blueprint(companies_route.main, url_prefix='/api/v_1/companies')
app.register_blueprint(auth_route.main, url_prefix='/api/v_1/auth')


if __name__ == '__main__':
    app.run(debug=True)
