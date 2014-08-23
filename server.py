from flask import Flask, request, Response, render_template
from app.blueprints.main import main
from app.blueprints.rider import rider_bp
from config.jinjacfg import setUpJinjaEnv
from config.settings import SETTINGS


app = Flask(__name__)
setUpJinjaEnv(app)
app.config.update(SETTINGS['dev'])

app.register_blueprint(main)
app.register_blueprint(rider_bp)

@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    if request.method == 'GET':
        return render_template('leaderboards.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
