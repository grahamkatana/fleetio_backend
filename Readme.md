# DB setup
you can use any database just install the specific drivers, this project supports pgsql and mysql as in the .env
# Running the project
### Create a virtual environmen ```python -m venv [env_name]```
### Activate the virtual environment
### Install the dependencies ```pip install -r requirements.txt```
# Runnig the migrations
### ``` in the console, project dir: run flask db init```
![Screenshot](__previews/Capture1.PNG)
### ``` in the console, project dir: run flask db migrate```
![Screenshot](__previews/Capture2.PNG)
### ``` in the console(update migrations), project dir: run flask db upgrade```
### If everything ran well, you can run the app ```python app.py```
![Screenshot](__previews/Capture3.PNG)

### DB Design
![Screenshot](__previews/db.png)
