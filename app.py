from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/employees", methods=['GET'])
def getEmployees():
    return jsonify('test')


@app.route("/employees", methods=['POST'])
def addEmployee():
    dane = request.get_json()
    return jsonify('test')


@app.route("/employees/:id", methods=['PUT'])
def changeEmployee():
    dane = request.get_json()
    return jsonify('test')


@app.route('/employees/:id', methods=["DELETE"])
def deleteEmployee():
    pass
