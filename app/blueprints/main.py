import socket
from flask import Blueprint, request, render_template, Response, redirect
from app.api.services.trial_service import TrialService
from websocket import create_connection


main = Blueprint('main', __name__,
                 template_folder='templates')

@main.record
def setup(state):
    main.trial_service = TrialService()
    try:
        main.ws = create_connection('ws://localhost:9000')
    except socket.error as e:
        print 'Connection Refused.  Is the socket server running?'
    except Exception as e:
        print e.message()


@main.route('/', methods=['GET'])
def index():
    return redirect('/trials/')




@main.route('/leaderboard/', methods=['GET'])
@main.route('/leaderboard/<string:trial_id>', methods=['GET'])
def leaderboard(trial_id=None):
    if request.method == 'GET':
        if trial_id:
            trial = main.trial_service.find(trial_id);
            return render_template('leaderboard.html', trial=trial)
        else:
            trials = main.trial_service.find({})
            return render_template('leaderboards.html', trials=trials)
