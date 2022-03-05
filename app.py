import flask

app = flask.Flask(__name__)
app.config["app"] = os.environ.get("APP", "app")
app.config["version"] = os.environ.get("VERSION", "0")
app.config["commit"] = os.environ.get("COMMIT", "00e8872b526c45e6272216ca57be60c00705b53f")
app.config["env"] = os.environ.get("ENV", "prod")

@app.route("/")
def up():
    return "hello world\n"
