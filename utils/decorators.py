from functools import wraps

from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth import auth


def validate_schema(schema_name):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            schema = schema_name()
            errors = schema.validate(request.get_json())
            if errors:
                raise BadRequest(f'{errors}')
            return function(*args, **kwargs)

        return wrapper

    return decorator


def permission_required(role):
    def decorated(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            current_user = auth.current_user()
            if not current_user.role == role:
                raise Forbidden('You don\'t have permission')
            return function(*args, **kwargs)

        return wrapper

    return decorated
