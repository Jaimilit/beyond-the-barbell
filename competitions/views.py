from django.shortcuts import render, redirect, get_object_or_404
from .models import Competition, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def competitions(request):
    """ A view to return the competitions page """
    competitions = Competition.objects.all()
    return render(request, 'competitions.html', {'competitions': competitions})

@login_required
def book_competition(request, competition_id):
    """Retrieves competition from the database and associates
    the booking with the current authenticated user"""
    competition = Competition.objects.get(id=competition_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.competition = competition
            booking_form.save()

            messages.success(request, 'Booking is confirmed')
            return redirect('booking_success')
    else:
        form = BookingForm()

    context = {
        'form': form,
        'competition': competition
    }
    return render(request, 'book_competition.html', context)


@login_required
def my_bookings(request):
    """A view to display bookings made by the current user."""
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=competition_id)
        return render(request, 'my_bookings.html', {'user_bookings': user_bookings})


def delete_booking(request, competition_id):
    """ Allows the user to delete a booking for a competition. """
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=competition_id)

        if booking.user == request.user:
            if request.method == "POST":
                booking.delete()
                return redirect('my_bookings')

            context = {'record': booking}
            return render(request, 'delete_booking.html', context)
        else:
            return redirect('my_bookings')
    else:
        return redirect('../accounts/signup')