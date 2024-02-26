from django import forms
from .models import Booking, Competition
from django.contrib.auth.models import User
from profiles.models import UserProfile 

class BookingForm(forms.ModelForm):
    """Create form for booking for user for competition"""
    class Meta:
        model = Booking
        exclude = ['user_profile']  # Exclude the user_profile field from the form
        labels = {
            'competition': 'Competition',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['competition'].queryset = Competition.objects.all()
