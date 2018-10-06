from flask import Flask, request, jsonify
import requests as req
from config import APP as config
import json
from sqlalchemy.sql import select, delete
from models import model as M
from pymongo import MongoClient
from flask_cors import CORS

client = MongoClient('mongodb://localhost:27017')

app = Flask(__name__)
CORS(app)

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
    if r.status_code == 200:
        rjson = r.json()['user']
        s = M.Session()
        query = select([M.User.__table__.c.session]).where(M.User.__table__.c.id==rjson['id'])
        us = s.execute(query).fetchone()
        if us:
            return jsonify({'session': us[0]})
        u = M.User(id=rjson['id'], loginName=rjson['loginName'], name="%s %s" % (rjson['name']['first'], rjson['name']['first']), roleType=rjson['roleType'], session=rjson['session']['userSession'])
        s.add(u)
        s.commit()
        return jsonify({'session': rjson['session']['userSession']})

@app.route('/logout', methods=['POST'])
def logout():
    usersession = request.headers.get('session')
    print("HEADERS", include_session(usersession))
    r = req.post('https://developer.api.yodlee.com:443/ysl/user/logout',
        headers=include_session(usersession))
    if r.status_code == 204:
        s = M.Session()
        s.execute(M.User.__table__.delete().where(M.User.__table__.c.session==usersession))
        s.commit()
        return jsonify({"message": "Logged out"})
app.run(debug=True)
