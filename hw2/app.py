import flask
from presenter import Presenter

app = flask.Flask(__name__)
presenter = Presenter()


@app.route('/')
def base():
    return flask.render_template(presenter.base())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
