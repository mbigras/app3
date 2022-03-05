import flask

app = flask.Flask(__name__)

@app.route("/")
def up():
    return "hello world\n"
