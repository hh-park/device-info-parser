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

todos = {}
count = 1
json_dict = {}

@api.route('/db')
class RestApi(Resource):

    def get(self):

        global json_dict

        json_dict = utils.get_json_data(file_name)
        inv_db_session = utils.db_create_session(db_host,db_id,db_pw,test_db)
        query = f'''
            select *
            from test.device
        '''
        res = utils.db_select_query(query, inv_db_session)




if __name__ == "__main__":

    app.run(debug=True, port=80)
