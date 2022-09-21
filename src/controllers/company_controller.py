from flask import jsonify, current_app
from config import db
from utils.send_email import send_email
from models.Company import Company
from utils.database_operations import save_record
from utils.rand_string_generator import get_random_string
from utils.messages import greet_get_time, message
from utils.file_uploads import upload_client_files
from models.Company import Company
from sqlalchemy.sql import text


def index():
    fetched_data = []
    companies = Company.query.filter_by(
        active=True).order_by(text("name desc")).all()
    for company in companies:
        fetched_data.append({
            'id': company.id,
            'company_name': company.name,
            'address': company.address,
            'country': company.country,
            'tags': company.tags,
            'company_type': company.company_type,
            'industry_type': company.industry_type,
            'latitude': company.latitude,
            'longitude': company.longitude,
            'logo': company.logo,
            'joined':company.createdAt

        })
      

    if companies:
        return jsonify({
            "data": fetched_data
        }), 200
    return jsonify({
        "data": fetched_data
    }), 200


def create(request, authenticated_email, name):
    try:
        unique_key = get_random_string(45)
        destination = "/logos"
        file_location = upload_client_files(request=request, destination=destination,
                                            client_message="Your company was successfully registered", error_message="There was an error uploading the file")
        if file_location != "error":
            print(request.form['name'])
            company = Company(active=False, name=request.form['name'], address=request.form['address'], country=request.form['country'], tags=request.form['tags'], company_type=request.form['company_type'], industry_type=request.form[
                              'industry_type'], latitude=request.form['latitude'], longitude=request.form['longitude'], logo=f"{current_app.config['UPLOAD_FOLDER'][1:]}{destination}/{file_location}", unique_access=unique_key.replace(" ", "_"))
            save_record(company, db)
            greeting = greet_get_time()
            send_email(recipients=authenticated_email,
                       message=f"{greeting} {name}! Thank you for registering a company under FleetIO. To make your company visible or active please pay the registration fee.", subject="Company registered to FleetIO", sender="app@fleetio.com")
            return message("Company was successfully registered", 201)
        else:
            return message("Error in creating the company", 400)

    except Exception as e:
        return message(str(e), 500)


def show():
    pass


def delete():
    pass
