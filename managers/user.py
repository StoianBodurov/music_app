from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash, generate_password_hash

from db import db
from managers.auth import AuthManager
from models import UserModel


class UserManager:
    @staticmethod
    def register(user_data):
        if UserModel.query.filter_by(email=user_data['email']).first():
            raise BadRequest('User already exist')

        user_data['password'] = generate_password_hash(user_data['password'], method='sha256')
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.flush()
            return AuthManager.encode_token(user)
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def login(user_data):
        try:
            user = UserModel.query.filter_by(email=user_data['email']).first()
            if user and check_password_hash(user.password, user_data['password']):
                return AuthManager.encode_token(user)
            raise Exception
        except Exception:
            raise BadRequest('Invalid username or password')
