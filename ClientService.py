import json
from flask import Flask, request
from flask_restx import Api, Resource
from InvConfig import CONFIG
import DeviceService as utils

db_host = CONFIG['db_ip']
db_id = CONFIG['db_id']
db_pw = CONFIG['db_pw']
test_db = CONFIG['test_db']
file_name = CONFIG['file_name']

app = Flask(__name__)
api = Api(app)

json_dict = {}

@api.route('/db')
class RestApi(Resource):

    def get(self):

        global json_dict

        db_session = utils.db_create_session(db_host,db_id,db_pw,test_db)
        json_dict = utils.get_json_data(file_name)

        for id in json_dict:

            device = json_dict[id]
            if not device['coordinates']:
                device['coordinates'] = [0, 0]

            query = f'''
                select *
                from test.device
                where id = '{id}';
            '''
            res = utils.db_select_query(query, db_session)

            if res:
                update_query = f'''
                    UPDATE test.device 
                    SET id = '{device['id']}', type = '{device['type']}', coordinates1 = {device['coordinates'][0]}, 
                    coordinates2 = {device['coordinates'][1]}, status = '{device['status']}', timezone = '{device['timezone']}'
                    WHERE id = '{id}';
                '''
                utils.db_insert_query(update_query, db_session)

            else:
                insert_query = f'''
                    INSERT INTO test.device 
                    VALUES ('{device['id']}', '{device['type']}', {device['coordinates'][0]}, {device['coordinates'][1]}, 
                        '{device['status']}', '{device['timezone']}')
                '''
                utils.db_insert_query(insert_query,db_session)

if __name__ == "__main__":

    app.run(debug=True, port=80)
