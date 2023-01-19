import time
from app import bucket
from flask import current_app
from sqlalchemy import event
from sqlalchemy.engine import Engine
from werkzeug.utils import secure_filename


@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement,
                          parameters, context, executemany):
    if not current_app.config['TESTING']:
        print(statement, parameters)
    conn.info.setdefault('query_start_time', []).append(time.time())


@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement,
                         parameters, context, executemany):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    if not current_app.config['TESTING']:
        print(total)


def save_data_s3(file, current_user):
    file.filename = secure_filename(file.filename)
    file.filename = f"photos/{current_user.id}/{file.filename}"
    bucket.upload_file_to_s3(file)
    url = f"https://lazoryktrust.s3.us-east-1.amazonaws.com/{file.filename}"
    return url
