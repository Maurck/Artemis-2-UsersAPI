'''
config.py: modulo donde se configura la aplicación
'''
import os
from dotenv import load_dotenv
from flask_cors import CORS
from mongoengine import connect

def config_app(app):
    load_dotenv()

    app.secret_key = os.getenv('SECRET_KEY')
    
    token_config(app)

    DB_URI = os.getenv('DB_URI')
    connect(host=DB_URI)

    CORS(app=app, supports_credentials=True)

def config_app_production(app):
    config_app(app)

    app.config.update(
        SERVER_NAME=os.getenv('PRODUCTION_SERVER_NAME'),
        SESSION_COOKIE_NAME=os.getenv('PRODUCTION_SERVER_NAME'),
        SESSION_COOKIE_DOMAIN=os.getenv('PRODUCTION_SERVER_NAME')
    )

def config_app_development(app):
    config_app(app)

    app.config.update(
        SERVER_NAME=os.getenv('DEVELOPMENT_SERVER_NAME'),
        SESSION_COOKIE_NAME=os.getenv('DEVELOPMENT_SERVER_NAME'),
        SESSION_COOKIE_DOMAIN=os.getenv('DEVELOPMENT_SERVER_NAME'),
    )

def token_config(app):
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
