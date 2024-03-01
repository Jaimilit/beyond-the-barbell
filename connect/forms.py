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
    """To write review of trainer"""
    class Meta:
        model = TrainerReview
        fields = ['title', 'content', 'trainer', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        rating_choices = TrainerReview.RATING_CHOICES
        self.fields['rating'].widget = forms.Select(choices=rating_choices)