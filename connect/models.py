from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """ Contact Form """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=230)
    message = models.TextField(max_length=2000)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']