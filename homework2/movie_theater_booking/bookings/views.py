from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    # Handles listing all movies, creating new ones, etc.
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    # Handles checking seat availability and booking seats
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    # handles viewing booking history and creating new bookings
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def movie_list(request):
    # Get all movies from the database
    movies = Movie.objects.all()
    # Send them to the template
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request, movie_id):
    # We will pass the movie_id so the user knows what they are booking
    return render(request, 'bookings/seat_booking.html', {'movie_id': movie_id})

def booking_history(request):
    return render(request, 'bookings/booking_history.html')