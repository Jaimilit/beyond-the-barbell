from django.shortcuts import render, redirect
from .models import Competition, Booking
from .forms import BookingForm

# Create your views here.

def competitions(request):
    """ A view to return the competitions page """


    return render(request, 'competitions.html')



def book_competition(request, competition_id):
    competition = Competition.objects.get(id=competition_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.competition = competition
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
        
    return render(request, 'book_competition.html', {'form': form, 'competition': competition})
