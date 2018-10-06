from flask import Flask, request, jsonify
import requests as req
import config
import json
from models import model as M

app = Flask(__name__)

DEFAULT_HEADERS = {
    "Api-Version": "1.1",
    "Cobrand-Name": "restserver",
    "Authorization": "{cobSession=08062013_0:0ba7db6e6573371cfbb45af7cd97c81837feab68d4ca2fcddb04bdaf8e966ad6dc264348831bbd091acbb32d3e1b0fce8669b548c91dd4ee7c407d657a174736}",
    "Content-Type": "application/json"
}
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
        u = M.User(id=rjson['id'], loginName=rjson['loginName'], name="%s %s" % (rjson['name']['first'], rjson['name']['first']), roleType=rjson['roleType'], session=rjson['session']['userSession'])
        s.add(u)
        s.commit()
        return jsonify({'session': rjson['session']['userSession']})

app.run(debug=True)
