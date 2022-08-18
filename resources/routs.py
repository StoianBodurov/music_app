from resources.album import GetAllAlbumList, GetUserAlbumList, GetAlbum, UpdateAlbum, DeleteAlbum, CreateAlbum
from resources.auth import RegisterUser, LoginUser

routes = (
    (RegisterUser, '/register'),
    (LoginUser, '/login'),
    (GetAllAlbumList, '/'),
    (GetUserAlbumList, '/user'),
    (CreateAlbum, '/album/create'),
    (GetAlbum, '/album/<int:pk>'),
    (UpdateAlbum, '/album/<int:pk>/update'),
    (DeleteAlbum, '/album/<int:pk>/delete'),
)
