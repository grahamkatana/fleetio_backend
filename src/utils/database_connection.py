import json
import requests
import os


def get_connection_string():
    # TODO return connection string based on database
    #'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(user, password, server, port, db_name)
    driver = os.getenv("DATABASE_DRIVER")
    user = os.getenv('DATABASE_USER')
    password = os.getenv('DATABASE_PASSWORD')
    server = os.getenv('DATABASE_URL')
    port = os.getenv('DATABASE_PORT')
    db_name = os.getenv('DATABASE_NAME')
    db = ""
    if driver == "pgsql":
        conn = "postgresql+ psycopg2"
        db = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
            conn, user, password, server, port, db_name)
    elif driver == "mysql":
        conn = "mysql+pymysql"
        db = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
            conn, user, password, server, port, db_name)

    return db
