from flask.ext.restful import Resource, reqparse
from app.api.services.trial_service import TrialService

parser = reqparse.RequestParser()
parser.add_argument('city', type=str)
parser.add_argument('races', type=str, action='append')

class TrialREST(Resource):
    def __init__(self):
        self.service = TrialService()

    def get(self, id=None):
        if id:
            trial = self.service.find(id)
            return trial.to_json()
        else:
            trials = self.service.find()
            return trials.to_json()

    def post(self):
        args = parser.parse_args()
        saved = self.service.create(args)
        new_trial = self.service.find(saved.id)
        return new_trial.to_json()

    def put(self, id=None):
        args = parser.parse_args()
        if id:
            trial = self.service.update(id, args)
        else:
            trial = self.service.create(args)
        ret = self.service.find(trial.id)
        return ret.to_json()

    def delete(self, id):
        self.service.delete(id)
        return 'Delete success'
