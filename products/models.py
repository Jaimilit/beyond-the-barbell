from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    subscription = models.ForeignKey('Subscription', null=True, blank=True, on_delete=models.SET_NULL)
    personal_training_session = models.ForeignKey('PersonalTrainingSession', related_name='products', null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name
    

class Subscription(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_months = models.IntegerField(default=1)
    # You can add more fields specific to subscriptions

    def __str__(self):
        return self.name


class PersonalTrainingSession(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_in_minutes = models.IntegerField()
    instructor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name