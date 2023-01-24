from flask import Flask, jsonify, request
import os
from neo import Database

app = Flask(__name__)


uri = os.getenv('URI')
user = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

database = Database(uri, user, password)


@app.route("/employees", methods=['GET'])
def getEmployees():
    employees = database.getEmployees()
    result = [{'name': result['m']['name']} for result in employees]
    return jsonify(result)


@app.route("/employees", methods=['POST'])
def addEmployee():
    dane = request.get_json()
    name = dane['name']
    department = dane['department']
    result = database.addEmployee(name, department)
    return jsonify(result)


@app.route("/employees/:id", methods=['PUT'])
def changeEmployee():
    dane = request.get_json()
    return jsonify('test')


@app.route('/employees/:id', methods=["DELETE"])
def deleteEmployee():
    pass
