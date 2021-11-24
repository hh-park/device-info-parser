import pymysql
import json

def get_json_data(json_file):

    with open(json_file, 'r', encoding='UTF-8') as jf:
        return json.load(jf)


def db_create_session(host, db_id, db_pw, db):

    try:
        return pymysql.connect(host=host, user=db_id, passwd=db_pw, db=db, charset='utf8')

    except pymysql.Error as err:
        print(f'Something went wrong {err}')


def db_select_query(query, db):

    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        row = cursor.fetchall()

    except pymysql.Error as err:
        print("Something went wrong: {}".format(err))
        raise ("DbSelectError")

    return row


def db_insert_query(query, db_session):

    try:
        cursor = db_session.cursor()
        cursor.execute(query)
        id = cursor.lastrowid
        db_session.commit()
        return id

    except pymysql.Error as err:
        print("Something went wrong: {}".format(err))
        raise ("DbInsertError")