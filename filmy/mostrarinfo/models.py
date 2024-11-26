from django.db import models
from django.contrib.auth.models import User

class ToWatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s watchlist - Movie ID: {self.movie_id}"

    def get_movie_ids(self):
        return list(ToWatchList.objects.filter(user=self.user).values_list('movie_id', flat=True))

