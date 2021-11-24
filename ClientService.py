from flask import Flask, request
from flask_restx import Api, Resource
from DeviceService import DeviceHandler

app = Flask(__name__)
api = Api(app)

@api.route('/db')
class Requirement1(Resource):

    def get(self):

        json_dict = request.json.get('json_data')
        dh = DeviceHandler()
        dh.update_db(json_dict)

        return {
            "msg" : "DB updated successfully",
            "succ" : True
        }

@api.route('/id')
class Requirement2(Resource):

    def get(self):

        search_param = request.json.get('id')
        dh = DeviceHandler()
        res = dh.select_db(search_param)

        result ={}
        result['id'] = res[0]['id']
        result['type'] = res[0]['type']
        result['coordinates1'] = res[0]['coordinates1']
        result['coordinates2'] = res[0]['coordinates2']
        result['status'] = res[0]['status']
        result['timezone'] = res[0]['timezone']

        return {
            "msg" : "Searched device successfully",
            "succ" : True,
            "search_parameter" : search_param,
            "search_result" : result
        }
if __name__ == "__main__":

    app.run(debug=True, port=80)
