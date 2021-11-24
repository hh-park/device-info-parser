from flask import Flask, request
from flask_restx import Api, Resource
from DeviceService import DeviceHandler

app = Flask(__name__)
api = Api(app)

@api.route('/db')
class UpdateDB(Resource):

    def get(self):

        json_dict = request.json.get('json_data')
        dh = DeviceHandler()
        dh.update_db(json_dict)

        return {
            "msg" : "DB updated successfully",
            "succ" : True
        }

@api.route('/id', methods=['GET'])
class SelectID(Resource):

    def get(self):

        search_param = request.json.get('id')
        dh = DeviceHandler()
        res = dh.select_by_id(search_param)

        return {
            "msg" : "Searched device successfully",
            "succ" : True,
            "search_parameter" : search_param,
            "search_result" : res
        }

@api.route('/type', methods=['GET'])
class SelectType(Resource):

    def get(self):

        search_param = request.json.get('type')
        dh = DeviceHandler()
        res = dh.select_by_type(search_param)

        return {
            "msg" : "Searched device successfully",
            "succ" : True,
            "search_parameter" : search_param,
            "search_result" : res
        }

@api.route('/status', methods=['GET'])
class SelectStatus(Resource):

    def get(self):

        search_param = request.json.get('status')
        dh = DeviceHandler()
        res = dh.select_by_status(search_param)

        return {
            "msg" : "Searched device successfully",
            "succ" : True,
            "search_parameter" : search_param,
            "search_result" : res
        }

if __name__ == "__main__":

    app.run(debug=True, port=80)
