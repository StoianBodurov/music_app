from werkzeug.exceptions import NotFound

from db import db
from models import SongModel, AlbumModel
from utils.managers_helpers import delete_item, update_item, get_item


class SongManager:
    @staticmethod
    def get_songs_in_album(pk):
        return SongModel.query.filter_by(album_pk=pk)

    @staticmethod
    def create_song(data, album_id):
        if AlbumModel.query.filter_by(id=album_id).first():
            raise NotFound('Album not exist')

        data['album_id'] = album_id
        song = SongModel(**data)
        db.session.commit(song)
        db.session.flush()
        return song

    @staticmethod
    def get_song(pk):
        return get_item(SongModel, pk)

    @staticmethod
    def update_song(data, pk):
        return update_item(SongModel, data, pk)

    @staticmethod
    def delete_song(pk):
        delete_item(SongModel, pk)

