# from config.db import db


def save_record(record,db):
    db.db.session.add(record)
    db.db.session.commit()
    db.db.session.refresh(record)
   
    try:
        return {
            'created': True,
            'data':record
        }, 201
    except:
        return {
            'created': False

        }, 429
