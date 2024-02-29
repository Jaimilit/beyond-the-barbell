from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .forms import ReviewForm
from .models import TrainerReview
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required




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
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
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
    review = get_object_or_404(TrainerReview, pk=review_id)
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
    # Retrieve the review object
    review = get_object_or_404(TrainerReview, pk=review_id)
    
    # Check if the logged-in user is the author of the review
    if review.user_profile.user != request.user:
        # If not the author, return an error or handle it as needed
        return HttpResponseForbidden("You are not authorized to delete this review.")

    if request.method == 'POST':
        # If a POST request is received, proceed with deletion
        review.delete()
        messages.success(request, 'Your review has been deleted successfully.')
    else:
        # If not a POST request, return to the reviews page
        messages.error(request, 'Invalid request method.')
    return redirect('reviews')  # Redirect to the reviews page after deletion

"""
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(TrainerReview, pk=review_id, user_profile=request.user.userprofile)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted successfully.')
        return redirect('reviews')
    return render(request, 'delete_review.html', {'review': review})
"""

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
