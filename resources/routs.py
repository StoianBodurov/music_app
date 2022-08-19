from resources.album import GetAllAlbumList, GetUserAlbumList, AlbumManagement, CreateAlbum
from resources.auth import RegisterUser, LoginUser

routes = (
    (RegisterUser, '/register'),
    (LoginUser, '/login'),
    (GetAllAlbumList, '/'),
    (GetUserAlbumList, '/user'),
    (CreateAlbum, '/album/create'),
    (AlbumManagement, '/album/<int:pk>'),
)
