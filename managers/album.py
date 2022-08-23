import os
import uuid

from werkzeug.exceptions import NotFound

from constant import TEMP_FILE_DIR
from db import db
from models import AlbumModel
from services.s3 import S3Service
from utils.helpers import decode_photo
from utils.managers_helpers import delete_item, update_item, get_item


s3 = S3Service()


def photo_processing(data):
    photo = data.pop('photo')
    extension = data.pop('photo_extension')
    file_name = f'{str(uuid.uuid4())}.{extension}'
    path = os.path.join(TEMP_FILE_DIR, file_name)
    decode_photo(path, photo)
    url = s3.upload_photo(path, file_name)
    return url, path, file_name


class AlbumManager:
    @staticmethod
    def get_all_album(user_id=None):
        if user_id:
            return AlbumModel.query.filter_by(user_id=user_id)
        return AlbumModel.query.all()

    @staticmethod
    def create_album(data, user_id):
        data['user_id'] = user_id
        url, path, file_name = photo_processing(data)
        try:
            data['img_url'] = url
            album = AlbumModel(**data)
            db.session.add(album)
            db.session.flush()
            return album
        except Exception:
            s3.delete_photo(file_name)
        finally:
            os.remove(path)

    @staticmethod
    def get_album(pk):
        return get_item(AlbumModel, pk)

    @staticmethod
    def update_album(data, pk):
        old_album = AlbumModel.query.filter_by(id=pk).first()
        if not old_album:
            raise NotFound('Item not exist')

        old_file_name = old_album.img_url.split('/')[-1]
        url, path, file_name = photo_processing(data)
        try:
            data['img_url'] = url
            album = update_item(AlbumModel, data, pk)
            s3.delete_photo(old_file_name)
            return album
        except Exception:
            s3.delete_photo(file_name)
        finally:
            os.remove(path)

    @staticmethod
    def delete_album(pk):
        album = AlbumModel.query.filter_by(id=pk).first()
        if not album:
            raise NotFound('Item not exist')
        file_name = album.img_url.split('/')[-1]
        delete_item(AlbumModel, pk)
        s3.delete_photo(file_name)

