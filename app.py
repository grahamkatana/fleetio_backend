import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_cors import CORS
from routes import auth_route, companies_route
from config.db import db, migrate
from config.mail import mail
from config.bcrypt import bcrypt
from utils.database_connection import get_connection_string

# app declaration
app = Flask(__name__)
CORS(app)
load_dotenv()

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# mail configuration
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')

# initialize the database
db.init_app(app)
migrate.init_app(app, db)
mail.init_app(app)
bcrypt.init_app(app)

# db.create_all()


# @app.route('/',methods=['GET','POST'])
# def index():
#     # request.method == 'POST'
#     return '<h1>Flask</h1>'

# company route
app.register_blueprint(companies_route.main, url_prefix='/api/v_1/companies')
app.register_blueprint(auth_route.main, url_prefix='/api/v_1/auth')


if __name__ == '__main__':
    app.run(debug=True)
