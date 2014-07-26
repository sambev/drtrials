from flask import Flask, request, Response, render_template
from app.blueprints.main import main
from config.jinjacfg import setUpJinjaEnv
from config.settings import SETTINGS


app = Flask(__name__)
setUpJinjaEnv(app)
app.config.update(SETTINGS['dev'])

app.register_blueprint(main)

if __name__ == "__main__":
    app.run()
