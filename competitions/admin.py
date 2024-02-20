from django.contrib import admin
from .models import Booking, Competition


@admin.register(Competition)
# Create competitiom optiomns in admin panel
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )


@admin.register(Booking)
# Create booking opporunities based on the competitions in admin panel
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'competition')
    list_filter = ('user', 'competition')
