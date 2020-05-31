import os
from flask import Flask
from config import Config
from flask_cors import CORS
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_app.shared.models import db
from flask_httpauth import HTTPBasicAuth
from utils.make_celery import make_celery

APP_ROOT = os.path.join(os.path.dirname(__file__), '../')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config.from_object(Config)

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet", cookie=None)
db.init_app(app)
auth = HTTPBasicAuth()
celery = make_celery(app)
migrate = Migrate(app, db)

CORS(app, supports_credentials=True)

from flask_app.api import api

app.register_blueprint(api, url_prefix='/api')
CORS(api)

from flask_app.auth import authenticate
from flask_app.auth.models import *

app.register_blueprint(authenticate, url_prefix='/api/auth')
CORS(authenticate)


@app.before_first_request
def your_function():
    print("first load")
