from flask import Blueprint

authenticate = Blueprint('auth', __name__)

from flask_app.auth import routes
