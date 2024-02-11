from django.contrib import admin
from .models import Product, Category, Subscription, PersonalTrainingSession

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class SubscriptionAdmin(admin.ModelAdmin):
      list_display = (
        'name',
        'description',
        'price',
        'duration_months',
    )

class PersonalTrainingSessionAdmin(admin.ModelAdmin):
      list_display = (
        'product',
        'description',
        'price',
        'duration_in_minutes',
        'instructor_name',
    )

   
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(PersonalTrainingSession, PersonalTrainingSessionAdmin)