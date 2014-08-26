from flask.ext.restful import Resource, reqparse
from app.api.services.rider_service import RiderService
from util.parse import parse_mongo_resp

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('number', type=int)
parser.add_argument('bike_type', type=str)
parser.add_argument('races', type=list)


class RiderREST(Resource):
    def __init__(self):
        self.service = RiderService()

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
        return parse_mongo_resp(new_trial)

    def put(self, id=None):
        args = parser.parse_args()
        if id:
            rider = self.service.update(id, args)
        else:
            rider = self.service.create(args)
        rider = self.service.find(rider.id)
        return parse_mongo_resp(rider)

    def delete(self, id):
        self.service.delete(id)
        return 'Delete success'
