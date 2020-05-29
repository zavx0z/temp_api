import os


class Config(object):
    DEBUG = os.getenv('DEBUG') or False
    SECRET_KEY = os.getenv('SECRET_KEY')
    CORS_HEADERS = 'Content-Type'
    # database
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or False
