'''Archivo que ejecuta la aplicacion'''
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from config.config import server_config
from config.config import get_app
from config.config import run_app
from routes.user import create_routes_user

app = get_app(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

server_config(app)
create_routes_user(app, bcrypt)

if __name__ == '__main__':
    run_app(app)
