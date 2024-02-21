from django.db import models
from django.utils import timezone
from profiles.models import UserProfile 



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
    trainer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title