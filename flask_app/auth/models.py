from random import randint

from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context

from flask_app import app
from flask_app.shared.models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), index=True, unique=True)

    is_superuser = db.Column(db.Boolean, default=False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=60 * 60 * 240):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        token = s.dumps({'id': self.id})
        return token, expiration

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    @staticmethod
    def generate_random_code():
        random = randint(1000, 9999)
        return random

    def __repr__(self):
        return f'<User {self.login}>'
