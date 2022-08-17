from flask import request

from managers.album import AlbumManager
from managers.auth import auth


class GetAllAlbumList:
    def get(self):
        pass


class GetUserAlbumList:
    @auth.login_required()
    def get(self):
        pass


class CreateAlbum:
    @auth.login_required
    def post(self):
        data = request.get_json()
        user = auth.current_user()
        album = AlbumManager.add_album(data, user.id)
        return album


class GetAlbum:
    def get(self):
        pass


class UpdateAlbum:
    def put(self):
        pass


class DeleteAlbum:
    def delete(self):
        pass
