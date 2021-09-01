from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/calculate")
def calculate():
    content = request.json
    print(content)
    return jsonify({
        "Hello"
    })
