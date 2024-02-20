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
    class Meta:
        model = TrainerReview
        fields = ['title', 'content', 'rating']