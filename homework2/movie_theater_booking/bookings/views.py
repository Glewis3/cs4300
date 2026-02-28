from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# --- API ViewSets ---
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# --- UI Views ---
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request, movie_id):
    # This is the line that was crashing! The import at the top fixes it.
    movie = get_object_or_404(Movie, id=movie_id) 
    available_seats = Seat.objects.filter(is_booked=False)
    
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        seat = get_object_or_404(Seat, id=seat_id)
        user = User.objects.first() 
        
        if user and not seat.is_booked:
            Booking.objects.create(movie=movie, seat=seat, user=user)
            seat.is_booked = True
            seat.save()
            return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': available_seats})

def booking_history(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def cancel_booking(request, booking_id):
    if request.method == 'POST':
        # Find the specific ticket
        booking = get_object_or_404(Booking, id=booking_id)
        
        # Free up the seat
        seat = booking.seat
        seat.is_booked = False
        seat.save()
        
        # Delete the ticket
        booking.delete()
        
    return redirect('booking_history')