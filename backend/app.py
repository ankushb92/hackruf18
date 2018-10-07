from flask import Flask, request, jsonify, make_response
import requests as req
from config import APP as config
import json
from pymongo import MongoClient
from dateutil import parser
import random
from flask_cors import CORS
from fake import Faker
from parse import Parser
from neural_net import predict, train

client = MongoClient('mongodb://localhost:27017')
db = client['monies']
users = db['users']
transactions = db['transactions']
holdings = db['holdings']

app = Flask(__name__)
CORS(app)

alphabet = 'qwertyuiopasdfghjklzxcvbnm'
def commit_fraud(uid):
    f = Faker(user_type=random.choice([1,2,3]))
    transactions.insert_one({**{'_id': uid}, **f.fake_transaction_history()})
    holdings.insert_one({**{'_id': uid}, **f.fake_holdings()})
    
DEFAULT_HEADERS = {
    "Api-Version": "1.1",
    "Cobrand-Name": "restserver",
    "Authorization": "{cobSession=%s}" % config['session']['cobSession'],
    "Content-Type": "application/json"
}

def flatten(l):
    return [i for s in l for i in s]

def include_session(s):
    auth_header = {'Authorization':  "{cobSession=%s,userSession=%s}" % (config['session']['cobSession'], s)}
    return {**DEFAULT_HEADERS, **auth_header}

def get_id_from_session(session):
    try:
        uid = list(users.find({'session.userSession': session}, {'_id': 1}))[0]['_id']
        return uid
    except IndexError:
        return None

def clean_json(allowed_keys, update_data, original_data):
    print(allowed_keys, update_data, original_data)
    def w(klist, data):
        for k in klist:
            data = data[k]
        return data
            
    for klist in allowed_keys:
        try:
            subobj = original_data
            for i, key in enumerate(klist):
                if i == (len(klist)-1):
                    subobj[key] = w(klist, update_data)
                elif key not in subobj:
                    subobj[key] = {}
                subobj = subobj[key]

        except KeyError:
            print("BAD KLIST", klist)
            continue
    return original_data

        
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
            users.update({'_id': rjson['id']},
                {'$set': {'session.userSession': rjson['session']['userSession']}})
            return jsonify(list(users.find({'_id': rjson['id']}).limit(1))[0])
        else:
            rjson['_id'] = rjson.pop('id')
            print("RSJON", rjson)
            users.insert_one(rjson)
            return jsonify(rjson)

@app.route('/user/update', methods=['PUT', 'POST'])
def update_user():
    uid = get_id_from_session(request.headers.get('session'))
    if not uid:
        return jsonify({"message": "bad user session token"}), 400
    user = list(users.find({'_id': uid}).limit(1))[0]
    allowed_keys = [x.split('.') for x in flatten([['dob'], ['name.%s' % n for n in ['first', 'last']],
        ['preferences.%s' % p for p in ['currency', 'timeZone']]])]
    request.data = clean_json(allowed_keys, json.loads(request.data), user)
    if 'dob' in request.data:
        request.data['dob'] = str(parser.parse(request.data['dob']))
    users.update_one({'_id': uid}, {'$set': request.data})
    return jsonify(list(users.find({'_id': uid}).limit(1))[0]), 200

@app.route('/transactions', methods=['GET'])
def get_transactions():
    session = request.headers.get("session")
    try:
        uid = list(users.find({'session.userSession': session}, {'_id': 1}))[0]['_id']
        transaction_results = list(transactions.find({'_id': uid},
            {'transaction': 1, '_id': 0}).limit(1))[0]
        transaction_results['transaction'] = list(reversed(transaction_results['transaction']))
        return jsonify(transaction_results), 200
    except IndexError:
        return jsonify({"message": "Invalid user session"}), 400

@app.route('/holdings', methods=['GET'])
def get_holdings():
    session = request.headers.get('session')
    try:
        uid = list(users.find({'session.userSession': session}, {'_id': 1}))[0]['_id']
        holding_data = list(holdings.find({'_id': uid}, {'holding': 1, '_id': 0}).limit(1))[0]
        return jsonify(holding_data)
    except IndexError:
        return jsonify({"message": "Invalid user session token"}), 400

@app.route('/accounts', methods=['GET'])
def get_accounts():
    session = request.headers.get('session')
    try:
        if len(list(users.find({'session.userSession': session}, {'_id': 1}))) > 0:
            r = req.get('https://developer.api.yodlee.com:443/ysl/accounts', headers=include_session(session))
            return jsonify(r.json()), 200
    except IndexError:
        return jsonify({"message": "Invalid user session token"}), 400

@app.route('/logout', methods=['POST'])
def logout():
    usersession = request.headers.get('session')
    r = req.post('https://developer.api.yodlee.com:443/ysl/user/logout',
        headers=include_session(usersession))
    if r.status_code == 204:
        users.update_one({'session.userSession': usersession},
            {'$set': {'session.userSession': ''.join([random.choice(alphabet) for _ in range(1024)])}})
        return jsonify({"message": "Logged out"})
    return jsonify({"message": "no"}), 404

@app.route('/portfolio', methods=['GET'])
def analyze_portfolio():
    uid = get_id_from_session(request.headers.get('session'))
    if not uid:
        return jsonify({"message": "Bad session :("}), 400
    p = Parser(list(transactions.find({'_id': uid}, {'transaction': 1, '_id': 0}))[0],
        list(holdings.find({'_id': uid}, {'holding': 1, '_id': 0}))[0], 25)
    pv, direction = predict(p.get_neural_net_attrs(), train())
    return jsonify({'fitness': pv[0], 'direction': direction.tolist()})
    
app.run(debug=True)
