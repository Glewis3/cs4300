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
    movie = get_object_or_404(Movie, id=movie_id)
    # Only show seats that haven't been booked yet
    available_seats = Seat.objects.filter(is_booked=False)
    
    # If the user clicks the 'Submit' button on the form
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        seat = get_object_or_404(Seat, id=seat_id)
        
        # Grab the first user in the database to act as our test user
        user = User.objects.first() 
        
        if user and not seat.is_booked:
            # Create the ticket!
            Booking.objects.create(movie=movie, seat=seat, user=user)
            # Mark the seat as taken
            seat.is_booked = True
            seat.save()
            # Send them to the history page to see their ticket
            return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': available_seats})

def booking_history(request):
    return render(request, 'bookings/booking_history.html')