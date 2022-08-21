from marshmallow import Schema, fields


class BaseSongSchema(Schema):
    name = fields.String(required=True)
    author = fields.String(required=True)