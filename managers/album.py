from db import db
from models import AlbumModel
from utils.managers_helpers import delete_item, update_item, get_item


class AlbumManager:
    @staticmethod
    def get_all_album(user_id=None):
        if user_id:
            return AlbumModel.query.filter_by(user_id=user_id)
        return AlbumModel.query.all()

    @staticmethod
    def create_album(data, user_id):
        data['user_id'] = user_id
        album = AlbumModel(**data)
        db.session.add(album)
        db.session.flush()
        return album

    @staticmethod
    def get_album(pk):
        # return AlbumModel.query.filter_by(id=pk).first()
        return get_item(AlbumModel, pk)

    @staticmethod
    def update_album(data, pk):
        # album = AlbumModel.query.filter_by(id=pk).first()
        # if not album:
        #     raise NotFound('Album not exist')
        # try:
        #     db.session.query(AlbumModel).filter(AlbumModel.id == pk).update(data)
        #     db.session.flush()
        #     return album
        # except Exception as ex:
        #     raise Exception(str(ex))
        return update_item(AlbumModel, data, pk)

    @staticmethod
    def delete_album(pk):
        # try:
        #     album = AlbumModel.query.filter_by(id=pk).first()
        #     db.session.delete(album)
        #     db.session.flush()
        # except Exception:
        #     raise NotFound('Album not exist')
        delete_item(AlbumModel, pk)
