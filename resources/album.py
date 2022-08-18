from flask import request
from flask_restful import Resource

from managers.album import AlbumManager
from managers.auth import auth
from schemas.response.album import ResponseAlbumSchema


class GetAllAlbumList(Resource):
    def get(self):
        albums = AlbumManager.get_all_album()
        return ResponseAlbumSchema().dump(albums, many=True)


class GetUserAlbumList(Resource):
    @auth.login_required
    def get(self):
        user_id = auth.current_user()
        albums = AlbumManager.get_all_album(user_id=user_id)
        return ResponseAlbumSchema().dump(albums, many=True)


class CreateAlbum(Resource):
    @auth.login_required
    def post(self):
        data = request.get_json()
        user = auth.current_user()
        album = AlbumManager.add_album(data, user.id)
        return ResponseAlbumSchema().dump(album)


class GetAlbum(Resource):
    def get(self, pk):
        album = AlbumManager.get_album(pk)
        return ResponseAlbumSchema().dump(album)


class UpdateAlbum(Resource):
    @auth.login_required
    def put(self, pk):
        data = request.get_json()
        album = AlbumManager.update_album(data, pk)
        return ResponseAlbumSchema().dump(album)


class DeleteAlbum(Resource):
    @auth.login_required
    def delete(self, pk):
        return AlbumManager.delete_album(pk)
