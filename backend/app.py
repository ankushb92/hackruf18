from flask import Flask, request, jsonify
import requests as req
from config import APP as config
import json
from pymongo import MongoClient
import random
from flask_cors import CORS
from fake import Faker

client = MongoClient('mongodb://localhost:27017')
db = client['monies']
users = db['users']
transactions = db['transactions']
holdings = db['holdings']

app = Flask(__name__)
CORS(app)

def commit_fraud(uid, tcount=0, hcount=0):
    print("Committing Fraud")
    tcount = tcount if tcount > 0 else random.randint(30, 100)
    hcount = hcount if hcount > 0 else random.randint(5, 50)
    f = Faker(tcount, hcount)
    transactions.insert_one({**{'_id': uid}, **f.fake_transaction_history()})
    holdings.insert_one({**{'_id': uid}, **f.fake_holdings()})
    
DEFAULT_HEADERS = {
    "Api-Version": "1.1",
    "Cobrand-Name": "restserver",
    "Authorization": "{cobSession=%s}" % config['session']['cobSession'],
    "Content-Type": "application/json"
}

def include_session(s):
    auth_header = {'Authorization':  "{cobSession=%s,userSession=%s}" % (config['session']['cobSession'], s)}
    return {**DEFAULT_HEADERS, **auth_header}

@app.route('/ping')
def pong():
    return jsonify({'message': 'Pong'})

@app.route('/login', methods=['POST'])
def login():
    request.data = json.loads(request.data)
    user_creds = {
    "user":
        {
            'loginName': request.data['username'],
            'password': request.data['password'],
            "locale": "en_US"
        }
    }
    r = req.post('https://developer.api.yodlee.com:443/ysl/user/login',
        data=json.dumps(user_creds), headers=DEFAULT_HEADERS)
    print("LOGIN", r.json()['user'])
    if r.status_code == 200:
        rjson = r.json()['user']
        if not list(transactions.find({"_id": rjson['id']})):
            commit_fraud(rjson['id'])
        if list(users.find({'_id': rjson['id']}).limit(1)):
            users.remove({'_id': rjson['id']})
        rjson['_id'] = rjson.pop('id')
        print("RSJON", rjson)
        users.insert_one(rjson)
        return jsonify(rjson)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    session = request.headers.get("session")
    try:
        uid = list(users.find({'session.userSession': session}, {'_id': 1}))[0]['_id']
        return jsonify(list(transactions.find({'_id': uid}, {'transaction': 1, '_id': 0}).limit(1))[0])
    except IndexError:
        return jsonify({"message": "Invalid user session"}), 400

@app.route('/holdings', methods=['GET'])
def get_holdings():
    session = request.headers.get('session')
    try:
        uid = list(users.find({'session.userSession': session}, {'_id': 1}))[0]['_id']
        return jsonify(list(transactions.find({'_id': uid}, {'holding': 1, '_id': 0}).limit(1))[0])
    except IndexError:
        return jsonify({"message": "Invalid user session token"}), 400

@app.route('/logout', methods=['POST'])
def logout():
    usersession = request.headers.get('session')
    print("HEADERS", include_session(usersession))
    r = req.post('https://developer.api.yodlee.com:443/ysl/user/logout',
        headers=include_session(usersession))
    if r.status_code == 204:
        users.remove({'session.userSession': usersession})
        return jsonify({"message": "Logged out"})
    return jsonify({"message": "no"}), 404
app.run(debug=True)
