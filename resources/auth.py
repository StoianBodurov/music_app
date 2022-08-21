from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.user import UserManager
from models import RoleType
from schemas.request.user import RegisterUserSchema, LoginUserSchema, RegisterAdminSchema
from utils.decorators import validate_schema, permission_required


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


class CreateAdmin(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(RegisterAdminSchema)
    def post(self):
        data = request.get_json()
        UserManager.create_admin(data)
        return 'created', 201
