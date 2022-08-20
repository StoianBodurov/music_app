from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import Unauthorized

from models import UserModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {
            'sub': (user.id, user.role.value),
            'exp': datetime.utcnow() + timedelta(hours=2)
        }
        return jwt.encode(payload, key=config("SECRET_KEY"), algorithm='HS256')

    @staticmethod
    def decode_token(token):
        try:
            data = jwt.decode(jwt=token, key=config("SECRET_KEY"), algorithms=['HS256'])
            return {'user_id': data['sub'][0], 'user_role': data['sub'][1]}
        except Exception as ex:
            raise ex


auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    try:
        token = AuthManager.decode_token(token)
        return UserModel.query.filter_by(id=token['user_id']).first()
    except Exception:
        raise Unauthorized('Invalid or missing token')
    