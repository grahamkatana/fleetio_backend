# from config.db import db


def save_record(record,db):
    db.db.session.add(record)
    db.db.session.commit()
    saved_id = record.id
    try:
        return {
            'created': True,
            'data':saved_id
        }, 201
    except:
        return {
            'created': False

        }, 429
