from flask import Flask, request, Response, render_template, make_response
from app.blueprints.main import main
from app.blueprints.trial import TrialREST
from app.blueprints.rider import RiderREST
from config.jinjacfg import setUpJinjaEnv
from config.settings import SETTINGS
from flask.ext.restful import Api


app = Flask(__name__)
api = Api(app)
setUpJinjaEnv(app)
app.config.update(SETTINGS['dev'])

app.register_blueprint(main)
api.add_resource(TrialREST, '/trials/<string:id>', '/trials/')
api.add_resource(RiderREST, '/riders/<string:id>', '/riders/')

@api.representation('text/html')
def output_html(data, code, headers=None):
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0')
