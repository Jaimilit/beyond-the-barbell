from django.db import models
from profiles.models import UserProfile
from django.contrib.auth.models import User


class Competition(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Competition, self).save(*args, **kwargs)


class Booking(models.Model):
    """This model provides the booking info for the user to
    book a competition"""
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.CASCADE,
                                     default=None)
    competition = models.ForeignKey(
        'Competition',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"{self.user_profile.username} booked {self.competition.title} "
        )

    def save(self, *args, **kwargs):
        super(Booking, self).save(*args, **kwargs)
