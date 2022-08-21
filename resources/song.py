from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.song import SongManager
from schemas.request.song import RequestSongSchema
from schemas.response.song import ResponseSongSchema
from utils.decorators import validate_schema


class GetAlbumSongList(Resource):
    def get(self, album_id):
        songs = SongManager.get_songs_in_album(album_id)
        return ResponseSongSchema().dump(songs, many=True)


class CreateSong(Resource):
    @auth.login_required
    @validate_schema(RequestSongSchema)
    def post(self, album_id):
        data = request.get_json()
        song = SongManager.create_song(data, album_id)
        return ResponseSongSchema().dump(song)


class SongManagement(Resource):
    def get(self, pk):
        song = SongManager.get_song(pk)
        return ResponseSongSchema().dump(song)

    @auth.login_required
    @validate_schema(RequestSongSchema)
    def put(self, pk):
        data = request.get_json()
        song = SongManager.update_song(data, pk)
        return ResponseSongSchema().dump(song)

    @auth.login_required
    def delete(self, pk):
        return SongManager.delete_song(pk)
