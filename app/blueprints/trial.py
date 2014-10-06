from flask.ext.restful import Resource, reqparse
from flask import request, render_template, redirect, Response
from util.request_helpers import wants_json
from util.parse import parse_mongo_resp
from util.sorts import sort_riders
from app.api.services.trial_service import TrialService
from app.api.services.rider_service import RiderService
from websocket import create_connection
import json

parser = reqparse.RequestParser()
parser.add_argument('city', type=str)
parser.add_argument('races', type=list)
parser.add_argument('riders', type=list)

class TrialREST(Resource):
    def __init__(self):
        self.service = TrialService()
        self.rider_service = RiderService()
        self.socket = create_connection('ws://localhost:9000')

    def get(self, id=None):
        if id:
            trial = json.loads(self.service.find(id).to_json())[0]
            trial['riders'] = sort_riders(trial['riders'])
            if wants_json(request.accept_mimetypes):
                return trial
            else:
                if trial:
                    return render_template('edit_trial.html', trial=trial)
                else:
                    return Response(status=404)
        else:
            trials = self.service.find()
            if wants_json(request.accept_mimetypes):
                return parse_mongo_resp(trials)
            else:
                return render_template('trials.html', trials=trials)

    def post(self):
        args = parser.parse_args()
        saved = self.service.create(args)
        new_trial = self.service.find(saved.id)
        self.update_socket(saved.id)
        if wants_json(request.accept_mimetypes):
            return parse_mongo_resp(new_trial)
        else:
            return redirect('/trials/%s' % new_trial[0].id, code=302)

    def put(self, id=None):
        args = parser.parse_args()
        if id:
            trial = self.service.update(id, args)
        else:
            trial = self.service.create(args)
        self.update_socket(trial.id)
        ret = self.service.find(trial.id)
        return parse_mongo_resp(ret)

    def delete(self, id):
        self.service.delete(id)
        self.update_socket(id)
        return 'Delete success'

    def update_socket(self, id):
        trial = json.loads(self.service.find(id).to_json())[0]
        trial['riders'] = sort_riders(trial['riders'])
        self.socket.send(json.dumps(trial))
