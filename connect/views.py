from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .forms import ReviewForm
from .models import TrainerReview


def contact(request, *args, **kwargs):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Message sent. Thank you! We will get back to you soon.'
                )
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Oops! That did not send. \
                    Check your details and try again.')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})

def reviews(request):
    # Your view logic goes here
    return render(request, 'reviews.html', context)
    

def submit_review(request, trainer_id):
    """ A view to handle the submission of trainer reviews """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.trainer_id = trainer_id
            review.save()
            messages.success(
                request,
                'Thank you for your review!'
            )
            return redirect(reverse('trainer_detail', args=[trainer_id]))
        else:
            messages.error(
                request, 'Oops! There was an error submitting your review. \
                    Please check your details and try again.'
            )
    else:
        form = ReviewForm()

    return render(request, 'reviews.html', {'form': form})