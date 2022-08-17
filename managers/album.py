from db import db
from models import AlbumModel


class AlbumManager:
    @staticmethod
    def get_all_album(user=None):
        if user:
            return AlbumModel.query.filter_by(user_id=user.id)
        return AlbumModel.query.all()

    @staticmethod
    def add_album(data, user_id):
        data['user_id'] = user_id
        album = AlbumModel(**data)
        db.session.commit(album)
        db.session.flush()
        return album

    @staticmethod
    def get_album(pk):
        return AlbumModel.query.filter_by(id=pk)

    @staticmethod
    def update_album(data, pk):
        db.session.query.filter(AlbumModel.id == pk).update(data)
        db.session.flush()
        return AlbumModel.filter_by(id=pk)

    @staticmethod
    def delete_album(pk):
        album = AlbumModel.query.filter_by(id=pk)
        db.session.delete(album)
        db.session.flush()
