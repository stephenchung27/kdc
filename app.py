import os
from flask import Flask, request, jsonify, send_from_directory
from api.kdc import KarutaDateCalculator
from datetime import datetime

app = Flask(__name__, static_folder="build")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route("/calculate", methods=['POST'])
def calculate():
    board = request.json

    duration = datetime.now()

    kdc = KarutaDateCalculator()
    kdc(board, board["direction"])

    duration = datetime.now() - duration

    app.logger.info("Took {} seconds".format(duration.seconds))

    return jsonify(kdc.optimal_route)
