from django import forms
from .models import Booking
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    """Create form for booking for user for competition"""
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'competition': 'competition',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)