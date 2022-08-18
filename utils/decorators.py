from functools import wraps

from flask import request
from werkzeug.exceptions import BadRequest


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
