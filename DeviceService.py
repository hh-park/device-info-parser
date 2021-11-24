import pymysql
import json
from InvConfig import CONFIG

json_dict = {}

db_host = CONFIG['db_ip']
db_id = CONFIG['db_id']
db_pw = CONFIG['db_pw']
test_db = CONFIG['test_db']
file_name = CONFIG['file_name']

class Utils(object):

    def get_json_data(self, json_file):

        with open(json_file, 'r', encoding='UTF-8') as jf:
            return json.load(jf)


    def db_create_session(self, host, db_id, db_pw, db):

        try:
            return pymysql.connect(host=host, user=db_id, passwd=db_pw, db=db, charset='utf8')

        except pymysql.Error as err:
            print(f'Something went wrong {err}')


    def db_select_query(self, query, db):

        try:
            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            row = cursor.fetchall()

        except pymysql.Error as err:
            print("Something went wrong: {}".format(err))
            raise ("DbSelectError")

        return row


    def db_insert_query(self, query, db):

        try:
            cursor = db.cursor()
            cursor.execute(query)
            id = cursor.lastrowid
            db.commit()
            return id

        except pymysql.Error as err:
            print("Something went wrong: {}".format(err))


class DeviceHandler(Utils):

    def update_db(self, json_dict):

        db_session = self.db_create_session(db_host,db_id,db_pw,test_db)
        for id in json_dict:

            device = json_dict[id]
            if not device['coordinates']:
                device['coordinates'] = [0, 0]

            query = f'''
                select *
                from test.device
                where id = '{id}';
            '''
            res = self.db_select_query(query, db_session)

            if res:
                update_query = f'''
                    UPDATE test.device 
                    SET id = '{device['id']}', type = '{device['type']}', coordinates1 = {device['coordinates'][0]}, 
                    coordinates2 = {device['coordinates'][1]}, status = '{device['status']}', timezone = '{device['timezone']}'
                    WHERE id = '{id}';
                '''
                self.db_insert_query(update_query, db_session)

            else:
                insert_query = f'''
                    INSERT INTO test.device 
                    VALUES ('{device['id']}', '{device['type']}', {device['coordinates'][0]}, {device['coordinates'][1]}, 
                        '{device['status']}', '{device['timezone']}')
                '''
                self.db_insert_query(insert_query,db_session)

    def select_by_id(self, search_param):

        db_session = self.db_create_session(db_host,db_id,db_pw,test_db)
        query = f'''
            select *
            from test.device
            where id = '{search_param}';
        '''
        res = self.db_select_query(query, db_session)
        return res

    def select_by_type(self, search_param):

        db_session = self.db_create_session(db_host,db_id,db_pw,test_db)
        query = f'''
            select *
            from test.device
            where type = '{search_param}';
        '''
        res = self.db_select_query(query, db_session)
        return res

    def select_by_status(self, search_param):

        db_session = self.db_create_session(db_host,db_id,db_pw,test_db)
        query = f'''
            select *
            from test.device
            where status = '{search_param}';
        '''
        res = self.db_select_query(query, db_session)
        return res