from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect 
from django.urls import reverse
from .models import Competition, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile



def competitions(request):
    """ A view to return the competitions page """
    competitions = Competition.objects.all()
    return render(request, 'competitions.html', {'competitions': competitions})

@login_required
def booking(request):
    """Retrieve workout sessions from the database, associate the booking with the current authenticated user"""
    competitions = Competition.objects.order_by('title')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is confirmed')
            return redirect('book_competition')  
    else:
        form = BookingForm()

    context = {
        'form': form,
        'competitions': competitions
    }
    return render(request, 'book_competition.html', context)  # 


@login_required
def book_competition(request, competition_id):
    """Book a competition for the authenticated user"""
    competition = get_object_or_404(Competition, id=competition_id)
    user_profile = UserProfile.objects.get(user=request.user)

    # Check if the user has already booked this competition
    existing_booking = Booking.objects.filter(user_profile=user_profile, competition=competition).first()
    if existing_booking:
        context = {'booked_competition': competition}
        return render(request, 'already_booked.html', context)  # Render already_booked.html page if already booked
    else:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user_profile = user_profile
                booking.competition = competition
                booking.save()
                messages.success(request, 'Booking is confirmed')
                return redirect('book_competition', competition_id=competition_id)  # Redirect to the same page after booking
        else:
            form = BookingForm()

        context = {
            'form': form,
            'competition': competition,
        }
        return render(request, 'book_competition.html', context)

"""
@login_required
def my_bookings(request):
    A view to display bookings made by the current user
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'user_bookings': user_bookings})
"""


@login_required
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
        return redirect('accounts:signup')