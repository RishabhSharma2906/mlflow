from flask import Flask, jsonify, json
from setupMongoDB import findConnection, createDatabase, listAllModels, insertRecordsModels
from bson import json_util

app = Flask(__name__)

@app.route('/')
def base():
    response = 'welcome to ML Service'
    return response, 200

@app.route('/listall')
def getListOfAllModels():
    all_models = insertRecordsModels()
    response_dict = {'model' : all_models }
    response = json_util.dumps(response_dict)
    return response, 200

if __name__ == "__main__":
    findConnection()
    insertRecordsModels()
    #createDatabase()
    #app.run(host="0.0.0.0", debug = True)
    app.run(host="0.0.0.0", port = 4000, debug = True)