from django.contrib import admin
from django.urls import path, include
from filmy.views import HomeScreen
from mostrarinfo.views import show_movie_info
from autenticacao.views import Login, Logout, Register
from userprofile.views import watchlist, remove_from_watchlist

urlpatterns = [
    path('logout/', Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name="Login"),
    path('filme/<int:movie_id>/', show_movie_info, name="show_movie_info"),
    path('', HomeScreen, name="HomeScreen"),
    path('admin/', admin.site.urls),
    path('profile/', watchlist, name="Profile"),
    path('profile/remove/', remove_from_watchlist, name='RemoveFromWatchlist'),
    path('register/', Register.as_view(), name='register'),
    path('mostrarinfo/', include('mostrarinfo.urls')),  # Incluindo as rotas do app mostrarinfo
]