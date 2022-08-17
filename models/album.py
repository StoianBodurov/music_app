from db import db


class AlbumModel(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
