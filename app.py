from flask import Flask
from starkintro.router.v1 import v1_blueprint

app = Flask(__name__)

app.register_blueprint(v1_blueprint)


@app.route('/')
def hello():
    return 'StarkIntro'
