from django import forms
from .models import Contact


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