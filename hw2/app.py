import flask
from presenter import Presenter

app = flask.Flask(__name__)
presenter = Presenter()


@app.route('/')
def index():
    return flask.render_template(presenter.index())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
