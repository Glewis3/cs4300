from behave import given, when, then
from bookings.models import Movie
from rest_framework.test import APIClient

@given('a movie named "{title}" exists in the database')
def step_create_movie(context, title):
    Movie.objects.create(
        title=title, 
        description="Blue aliens.", 
        release_date="2009-12-18", 
        duration=162
    )

@when('I request the movie list from the API')
def step_request_movies(context):
    context.client = APIClient()
    context.response = context.client.get('/api/movies/')

@then('I should receive a 200 status code')
def step_check_status(context):
    assert context.response.status_code == 200