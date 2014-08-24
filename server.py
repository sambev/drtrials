from flask import Flask, request, Response, render_template
from app.blueprints.main import main
from app.blueprints.rider import rider_bp
from app.blueprints.trial import TrialREST
from config.jinjacfg import setUpJinjaEnv
from config.settings import SETTINGS
from flask.ext.restful import Api


app = Flask(__name__)
api = Api(app)
setUpJinjaEnv(app)
app.config.update(SETTINGS['dev'])

app.register_blueprint(main)
app.register_blueprint(rider_bp)

api.add_resource(TrialREST, '/trial/<string:id>', '/trial/')

@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    if request.method == 'GET':
        return render_template('leaderboards.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
