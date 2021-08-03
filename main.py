import os
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
import json
from bson import json_util

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = os.environ['SECRET']
mongo = PyMongo(app)



@app.route('/', methods=['GET'])
def index():
    starttijd = mongo.db.tijden.find().sort("start", -1).limit(2)
    output = [{'starttijd' : doc['start'] } for doc in starttijd]
    return jsonify(output)


@app.route('/start', methods=['GET'])
def start():
    mongo.db.tijden.insert_one({'start': datetime.utcnow()});
    return  {'result' : 'Created successfully'}
