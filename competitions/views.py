from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Competition, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile


@login_required
def competitions(request):
    """ A view to render a list of competitions """
    if request.method == 'POST':
        competition_id = request.POST.get('competition_id')
        competition = get_object_or_404(Competition, id=competition_id)
        user_profile = request.user.userprofile

        # Check if the user has already booked this competition
        existing_booking = Booking.objects.filter(user_profile=user_profile, competition=competition).first()
        if existing_booking:
            messages.warning(
                request, 'You have already booked this competition.')
        else:
            booking = Booking(user_profile=user_profile,
                              competition=competition)
            booking.save()
            messages.success(request, 'Booking is confirmed.')
            return redirect('my_bookings')

    competitions = Competition.objects.all()
    return render(request, 'competitions.html', {'competitions': competitions})


@login_required
def booking(request, competition_id):
    """View for booking a specific competition"""
    competition = get_object_or_404(Competition, id=competition_id)
    user_profile = request.user.userprofile

    # Check if the user has already booked this competition
    existing_booking = Booking.objects.filter(user_profile=user_profile, competition=competition).first()
    if existing_booking:
        messages.warning(request, 'You have already booked this competition.')
        return redirect('my_bookings')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user_profile = user_profile
            booking.competition = competition
            booking.save()
            messages.success(request, 'Booking is confirmed.')
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form, 'competition': competition})


@login_required
def my_bookings(request):
    """View to display user bookings"""
    user_bookings = Booking.objects.filter(user_profile=request.user.userprofile)
    return render(request, 'my_bookings.html', {'user_bookings': user_bookings})


@login_required
def delete_booking(request, booking_id):
    """View to delete a booking"""
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST' and booking.user_profile.user == request.user:
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
    return redirect('my_bookings')
