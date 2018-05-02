import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'welcome to my first python site.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
