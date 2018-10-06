from flask import Flask, request, jsonify
import requests as req

app = Flask(__name__)

@app.route('/ping')
def pong():
    return jsonify({'message': 'Pong'})

app.run(debug=True)
