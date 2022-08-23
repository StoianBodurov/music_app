from marshmallow import fields

from schemas.base_album import BaseAlbumSchema


class RequestAlbumSchema(BaseAlbumSchema):
    photo = fields.String(required=True)
    photo_extension = fields.String(required=True)
