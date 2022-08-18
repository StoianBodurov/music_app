from marshmallow import Schema, fields


class BaseAlbumSchema(Schema):
    name = fields.String(required=True)
    img_url = fields.String(required=True)
    price = fields.Float(required=True)
    release_date = fields.String(required=True)
    artist = fields.String(required=True)
    genre = fields.String(required=True)
    description = fields.String(required=True)
