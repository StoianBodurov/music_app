from marshmallow import fields

from schemas.base_album import BaseAlbumSchema


class ResponseAlbumSchema(BaseAlbumSchema):
    id = fields.Integer(required=True)
