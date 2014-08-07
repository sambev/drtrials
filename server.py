from flask import Flask, request, Response, render_template
from app.blueprints.main import main
from config.jinjacfg import setUpJinjaEnv
from config.settings import SETTINGS


app = Flask(__name__)
setUpJinjaEnv(app)
app.config.update(SETTINGS['dev'])

app.register_blueprint(main)

@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    if request.method == 'GET':
        return render_template('leaderboards.html')


if __name__ == "__main__":
    app.run()
