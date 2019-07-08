from flask import Flask, request, make_response
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/unsafe')
def unsafe():
    first_name = request.args.get('name')
    return str(first_name)

if __name__ == "__main__":
    app.run(debug=True)
