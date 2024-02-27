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
    reviews = TrainerReview.objects.all()
    context = {'reviews': reviews}
    return render(request, 'reviews.html', context)


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Thank you for your review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Oops! There is an error with your review.'
                           'Please check your details and try again.')
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form})


def newsletter(request):
    """ A view to return the newsletter signup page """

    return render(request, 'newsletter.html')


def private_policy(request):
    """ A view to render the privacy statement in compliance with GDPR """

    return render(request, 'private_policy.html')
