from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from unittest.mock import patch
from django.contrib.auth.models import User
from mostrarinfo.models import ToWatchList

class ShowMovieInfoTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.movie_id = 123  # Example movie ID
        self.url = reverse('show_movie_info', args=[self.movie_id])
        self.user = User.objects.create_user(username='testuser', password='password')

    @patch('requests.get')
    def test_show_movie_info(self, mock_get):
        mock_movie_data = {
            'release_date': '2023-01-01',
            'title': 'Example Movie',
            'id': self.movie_id
        }
        mock_get.return_value.json.return_value = mock_movie_data

        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'showinfo.html')
        self.assertIn('filme', response.context)
        self.assertEqual(response.context['filme']['title'], 'Example Movie')
        self.assertEqual(response.context['filme']['release_date'], 'January 1, 2023')

    @patch('requests.get')
    def test_add_to_watchlist_authenticated(self, mock_get):
        self.client.login(username='testuser', password='password')
        mock_movie_data = {
            'release_date': '2023-01-01',
            'title': 'Example Movie',
            'id': self.movie_id
        }
        mock_get.return_value.json.return_value = mock_movie_data

        response = self.client.get(self.url + '?Add=True')
        self.assertRedirects(response, self.url)
        self.assertTrue(ToWatchList.objects.filter(user=self.user, movie_id=self.movie_id).exists())

    def test_add_to_watchlist_unauthenticated(self):
        response = self.client.get(self.url + '?Add=True')
        login_url = reverse('Login')
        self.assertRedirects(response, login_url)

