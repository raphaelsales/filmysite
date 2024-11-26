from django.shortcuts import render, redirect
from mostrarinfo.models import ToWatchList
from django.conf import settings
from django.urls import reverse
import requests
import datetime

def watchlist(request):
    if request.user.is_authenticated:
        movies = ToWatchList.objects.filter(user=request.user)
        movies_to_watch = []
        
        for movie in movies:
            url = f"{settings.API_SHOW_MOVIE_INFO_URL}"
            ondeInserirOID = url.find("/movie/") + len("/movie/")
            enderecoParaBuscarFilme = url[:ondeInserirOID] + str(movie.movie_id) + url[ondeInserirOID:]
            movie_info = requests.get(enderecoParaBuscarFilme).json()
            movies_to_watch.append(movie_info)
            
    
        context = {'movies': movies_to_watch, 'user': request.user}
        return render(request, 'profile.html', context)
    else:
        return render(request, 'login.html')

def remove_from_watchlist(request):
    if request.method == 'POST':
        filme_id = request.POST.get('filme_id')
        if request.user.is_authenticated:
            try:
                movie_to_delete = ToWatchList.objects.get(user=request.user, movie_id=filme_id)
                movie_to_delete.delete()
            except ToWatchList.DoesNotExist:
                pass
    return redirect(reverse('Profile'))
