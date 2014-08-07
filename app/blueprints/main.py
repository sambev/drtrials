import sys

from flask import Blueprint, request, render_template, Response
from websocket import create_connection

main = Blueprint('main', __name__,
                 template_folder='templates')

@main.record
def setup(state):
    main.ws = create_connection('ws://localhost:9000')

@main.route('/', methods=['GET'])
def index():
    """ Render the landing page """
    if request.method == 'GET':
        return render_template('index.html')

@main.route('/rider', methods=['POST'])
def rider():
    if request.method == 'POST':
        print request.form
        main.ws.send('Hi there')
        result = main.ws.recv()
        print result
        return Response('hi')
