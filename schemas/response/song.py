from marshmallow import fields

from schemas.base_song import BaseSongSchema


class ResponseSongSchema(BaseSongSchema):
    id = fields.Integer(required=True)