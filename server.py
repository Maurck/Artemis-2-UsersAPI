'''Archivo que ejecuta la aplicacion'''
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_bcrypt import Bcrypt

from config.config import server_config
from routes.user import create_routes_user

app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

server_config(app)
create_routes_user(app, bcrypt)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
