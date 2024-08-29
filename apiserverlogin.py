# app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import jwt
import datetime
import json

app = Flask(__name__)
CORS(app)

# Chave secreta para JWT
SECRET_KEY = '123'

# Dados de login (para fins de exemplo, use um banco de dados real em produção)
with open('login.json', 'r') as file:
    login_data = json.load(file)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == login_data['username'] and password == login_data['password']:
        token = jwt.encode({
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow()
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('', path)

if __name__ == '__main__':
    app.run(debug=True)
