
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_cors import CORS
from routes import companies_route
from config.db import db,migrate
from utils.database_connection import get_connection_string

app = Flask(__name__)
CORS(app)
load_dotenv()



app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app,db)

# db.create_all()



# @app.route('/',methods=['GET','POST'])
# def index():
#     # request.method == 'POST'
#     return '<h1>Flask</h1>'

app.register_blueprint(companies_route.main, url_prefix='/api/v_1/companies')


if __name__ == '__main__':
    app.run(debug=True)
