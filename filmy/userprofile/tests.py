from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from mostrarinfo.models import ToWatchList

class WatchlistTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.movie_id = 123  # Example movie ID
        ToWatchList.objects.create(user=self.user, movie_id=self.movie_id)

    def test_watchlist_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('Profile'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_watchlist_unauthenticated(self):
        response = self.client.get(reverse('Profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class RemoveFromWatchlistTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.movie_id = 123  # Example movie ID
        ToWatchList.objects.create(user=self.user, movie_id=self.movie_id)

    def test_remove_from_watchlist_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('RemoveFromWatchlist'), {'filme_id': self.movie_id})
        self.assertRedirects(response, reverse('Profile'))
        self.assertFalse(ToWatchList.objects.filter(user=self.user, movie_id=self.movie_id).exists())

    def test_remove_from_watchlist_unauthenticated(self):
        response = self.client.post(reverse('RemoveFromWatchlist'), {'filme_id': self.movie_id})
        self.assertRedirects(response, reverse('Profile'))
        self.assertTrue(ToWatchList.objects.filter(user=self.user, movie_id=self.movie_id).exists())
