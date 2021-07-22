'''Archivo que ejecuta la aplicacion'''
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_bcrypt import Bcrypt

from config.config import config_app_development
#from routes.views import create_routes_views
#from routes.bicycles import create_routes_bicycles
from routes.user import create_routes_user

#app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

config_app_development(app)
#create_routes_views(app)
#create_routes_bicycles(app)
create_routes_user(app, bcrypt)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
