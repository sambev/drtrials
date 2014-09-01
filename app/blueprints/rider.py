from flask.ext.restful import Resource, reqparse
from app.api.services.rider_service import RiderService
from util.parse import parse_mongo_resp
from websocket import create_connection

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('number', type=int)
parser.add_argument('bike_type', type=str)
parser.add_argument('races', type=list)


class RiderREST(Resource):
    def __init__(self):
        self.service = RiderService()
        self.socket = create_connection('ws://localhost:9000')

    def get(self, id=None):
        if id:
            rider = self.service.find(id)
            return parse_mongo_resp(rider)
        else:
            riders = self.service.find()
            return parse_mongo_resp(riders)

    def post(self):
        args = parser.parse_args()
        saved = self.service.create(args)
        new_trial = self.service.find(saved.id)
        self.update_socket()
        return parse_mongo_resp(new_trial)

    def put(self, id=None):
        args = parser.parse_args()
        if id:
            rider = self.service.update(id, args)
        else:
            rider = self.service.create(args)
        rider = self.service.find(rider.id)
        self.update_socket()
        return parse_mongo_resp(rider)

    def delete(self, id):
        self.service.delete(id)
        self.update_socket()
        return 'Delete success'

    def update_socket(self):
        riders = self.service.find()
        self.socket.send(riders.to_json())
