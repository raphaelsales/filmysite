from django.shortcuts import render
from django.conf import settings
import requests
import datetime

# Busca os filmes que serão lançados em breve
def get_upcoming_movies(url):
    response = requests.get(url)
    return response.json()

# Formata os filmes recebidos
def format_movies(movies):
    for movie in movies:
        movie['release_date'] = datetime.datetime.strptime(movie['release_date'], "%Y-%m-%d").date()
    return movies

# Determina o status do usuario
def get_user_status(request):
    return "Perfil" if request.user.is_authenticated else "Entrar"

# Main
def HomeScreen(request):
    url = f"{settings.API_UPCOMING_URL}&language=en-US&region=US&page=1"
    upcoming_movies_data = get_upcoming_movies(url)
    movies = format_movies(upcoming_movies_data['results'])
    EntrarOuPerfil = get_user_status(request)

    context = {
        'data_atual': datetime.datetime.now().date(),
        'dates': upcoming_movies_data['dates'],
        'movies': movies,
        'EntrarOuPerfil': EntrarOuPerfil,
    }

    return render(request, 'telainicial.html', context)
