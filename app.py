from ddtrace import config
from ddtrace import patch_all
from ddtrace import tracer

config.flask["service_name"] = "test-dd"
tracer.set_tags({"env": "local"})
patch_all(flask=True, requests=True)

from flask import Flask

from blueprint import bp

app = Flask(__name__)

app.register_blueprint(bp)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=8000)
