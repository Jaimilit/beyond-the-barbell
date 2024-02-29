from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .forms import ReviewForm
from .models import TrainerReview
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


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


@login_required
def submit_review(request):
    """ To be able to write a review as a logged in user """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_profile = request.user.userprofile  
            review.save()
            messages.success(request, 'Thank you for your review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Oops! There is an error with your review. Please check your details and try again.')
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form})


@login_required
def edit_review(request, review_id):
    """ To be able to edit only my own reviews as a logged in user """

    review = get_object_or_404(TrainerReview, pk=review_id)
    
    # Check if the logged-in user is the author of the review
    if review.user_profile != request.user.userprofile:
        error_message = "You are not authorized to edit this review."
        messages.error(request, error_message)
        return redirect(reverse('reviews'))  
        
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated successfully.')
            return redirect(reverse('reviews'))
    else:
        form = ReviewForm(instance=review)
    return render(request, 'submit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    """ A delete a review I've written as a logged in user """

    review = get_object_or_404(TrainerReview, pk=review_id)

    if review.user_profile != request.user.userprofile:
        error_message = "You are not authorized to delete this review."
        messages.error(request, error_message)
    else:
        if request.method == 'POST':
            review.delete()
            messages.success(request, 'Your review has been deleted successfully.')
            return redirect('reviews')
        else:
            messages.error(request, 'Invalid request method.')

    return redirect('reviews')


def reviews(request):
    """ View to display reviews """
    reviews = TrainerReview.objects.all() 
    context = {'reviews': reviews}
    return render(request, 'reviews.html', context)


def newsletter(request):
    """ A view to return the newsletter signup page """

    return render(request, 'newsletter.html')


def private_policy(request):
    """ A view to render the privacy statement in compliance with GDPR """

    return render(request, 'private_policy.html')
