from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie

class MovieIntegrationTests(APITestCase):
    def setUp(self):
        # Set up data for the whole test case
        self.movie = Movie.objects.create(
            title="Inception", 
            description="A thief who enters the dreams of others.", 
            release_date="2010-07-16", 
            duration=148
        )

    def test_get_movies_endpoint(self):
        # Test the API endpoint directly
        response = self.client.get('/api/movies/')
        
        # 1. Check Status Code (Ensure it returns 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. Check Data Format (Ensure it returns JSON)
        self.assertEqual(response['Content-Type'], 'application/json')
        
        # 3. Check Data Content
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Inception')

    def test_create_movie_endpoint(self):
        # Test POSTing data to the API
        new_movie_data = {
            "title": "Interstellar",
            "description": "Space travel.",
            "release_date": "2014-11-07",
            "duration": 169
        }
        response = self.client.post('/api/movies/', new_movie_data)
        
        # Check Status Code (Ensure it returns 201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)