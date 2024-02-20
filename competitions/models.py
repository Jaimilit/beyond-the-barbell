from django.db import models
from django.contrib.auth.models import User

class Competition(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='competitions/images/')


class Booking(models.Model):
    """This model provides the booking info for the user to
    book a competition"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(
        'competition',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"{self.user.username} booked {self.competition.title} "
        )

    def save(self, *args, **kwargs):
        super(Booking, self).save(*args, **kwargs)