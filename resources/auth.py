from flask import request
from flask_restful import Resource

from managers.user import UserManager
from schemas.request.user import RegisterUserSchema, LoginUserSchema
from utils.decorators import validate_schema


class RegisterUser(Resource):
    @validate_schema(RegisterUserSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)
        return {'token': token}, 201


class LoginUser(Resource):
    @validate_schema(LoginUserSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        return {'token': token}
