
#!flask/bin/python
from flask import Flask
from flask import render_template

from run import flaskrun

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/', methods=['POST'])
def post():
    return '{"Output":"Hello World"}'

if __name__ == '__main__':
    flaskrun(app)