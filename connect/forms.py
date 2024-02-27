from django import forms
from .models import Contact
from .models import TrainerReview


class ContactForm(forms.ModelForm):
    """
    Contact Form to contact us
    """
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ReviewForm(forms.ModelForm):
    """ Review form for reviewing Personal Trainers"""
    class Meta:
        model = TrainerReview
        fields = ['title', 'trainer', 'content', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        rating_choices = TrainerReview.RATING_CHOICES
        self.fields['rating'].widget = forms.Select(choices=rating_choices)
