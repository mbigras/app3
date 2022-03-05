import os

import flask
import arrow

app = flask.Flask(__name__)
app.config["app"] = os.environ.get("APP", "app")
app.config["version"] = os.environ.get("VERSION", "0")
app.config["commit"] = os.environ.get("COMMIT", "00e8872b526c45e6272216ca57be60c00705b53f")
app.config["build_time"] = arrow.get(os.environ.get("BUILD_TIME", "2022-03-05 19:12:07+00:00")).to("utc")
app.config["start_time"] = arrow.utcnow()
app.config["env"] = os.environ.get("ENV", "prod")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def up():
    request_time = arrow.utcnow()
    uptime = request_time - app.config["start_time"]
    return flask.jsonify(
        app=app.config["app"],
        version=app.config["version"],
        commit=app.config["commit"],
        env=app.config["env"],
        build_time=app.config["build_time"].format(arrow.FORMAT_RFC3339),
        start_time=app.config["start_time"].format(arrow.FORMAT_RFC3339),
        request_time=request_time.format(arrow.FORMAT_RFC3339),
        uptime=str(uptime),
        message="hello world!",
    )
