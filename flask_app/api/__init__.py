from flask import Blueprint

api = Blueprint('api', __name__)

from flask_app.api import routes
