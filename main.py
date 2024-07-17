import flask


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    flask.abort(401)
