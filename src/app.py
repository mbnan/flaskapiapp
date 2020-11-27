from flask import Flask , jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from FlaskAPI!'


@app.route('/home')
def home_page():
    return jsonify(message='Welcome to FlaskAPI home page $###')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
