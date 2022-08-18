from db import db
from models import AlbumModel


class AlbumManager:
    @staticmethod
    def get_all_album(user_id=None):
        if user_id:
            return AlbumModel.query.filter_by(user_id=user_id)
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
        return AlbumModel.query.filter_by(id=pk).first()

    @staticmethod
    def update_album(data, pk):
        db.session.query(AlbumModel).filter(AlbumModel.id == pk).update(data)
        db.session.flush()
        return AlbumModel.query.filter_by(id=pk).first()

    @staticmethod
    def delete_album(pk):
        album = AlbumModel.query.filter_by(id=pk).first()
        db.session.delete(album)
        db.session.flush()
