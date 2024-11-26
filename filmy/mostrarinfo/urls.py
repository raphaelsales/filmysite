from django.urls import path
from .views import show_movie_info, get_upcoming_movies, add_to_watchlist_v2

urlpatterns = [
    path('api/movies/', get_upcoming_movies, name='get-upcoming-movies'),  # Rota para filmes
    path('<int:movie_id>/', show_movie_info, name='show_movie_info'),  # Rota para detalhes do filme
    path('add-to-watchlist/', add_to_watchlist_v2, name='add_to_watchlist_v2'),  # Rota para adicionar à watchlist
]