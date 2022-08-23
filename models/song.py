from db import db


class SongModel(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id', ondelete='CASCADE'))
    album = db.relationship('AlbumModel')
