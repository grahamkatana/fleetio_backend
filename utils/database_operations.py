# from config.db import db


def save_record(record,db):
    db.db.session.add(record)
    db.db.session.commit()
    try:
        return {
            'created': True
        }, 201
    except:
        return {
            'created': False

        }, 429
