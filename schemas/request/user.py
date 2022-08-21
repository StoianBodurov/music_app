from marshmallow import fields, Schema, validate


class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=30))


class RegisterUserSchema(UserSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=30))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=30))
    phone = fields.String(required=True, validate=validate.Length(min=2, max=15))


class LoginUserSchema(UserSchema):
    pass


class RegisterAdminSchema(RegisterUserSchema):
    pass
