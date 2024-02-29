from django.db import models
from django.utils import timezone
from profiles.models import UserProfile
from django.contrib.auth.models import User



class Contact(models.Model):
    """ Contact Form """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=230)
    message = models.TextField(max_length=2000)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']




class TrainerReview(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        default=1,
        related_name='trainer_reviews'
    )
    # Your other fields
    trainer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.title
