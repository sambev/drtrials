import socket
from flask import Blueprint, request, render_template, Response
from websocket import create_connection

main = Blueprint('main', __name__,
                 template_folder='templates')

@main.record
def setup(state):
    try:
        main.ws = create_connection('ws://localhost:9000')
    except socket.error as e:
        print 'Connection Refused.  Is the socket server running?'
    except Exception as e:
        print e.message()


@main.route('/', methods=['GET'])
def index():
    """ Render the landing page """
    if request.method == 'GET':
        return render_template('rider.html')


@main.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    if request.method == 'GET':
        return render_template('leaderboard.html')
