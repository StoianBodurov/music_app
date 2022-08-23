from resources.album import GetAllAlbumList, GetUserAlbumList, AlbumManagement, CreateAlbum
from resources.auth import RegisterUser, LoginUser, CreateAdmin
from resources.song import GetAlbumSongList, CreateSong, SongManagement


routes = (
    (RegisterUser, '/register'),
    (LoginUser, '/login'),
    (GetAllAlbumList, '/'),
    (GetUserAlbumList, '/user'),
    (CreateAlbum, '/album/create'),
    (AlbumManagement, '/album/<int:pk>'),
    (GetAlbumSongList, '/album/<int:album_id>/songs'),
    (CreateSong, '/album/<int:album_id>/songs/create'),
    (SongManagement, '/songs/<int:pk>'),
    (CreateAdmin, '/admin/create'),
)
