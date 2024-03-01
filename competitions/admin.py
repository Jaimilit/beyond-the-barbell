from django.contrib import admin
from .models import Booking, Competition


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'competition')
    list_filter = ('competition',)

    def user_profile(self, obj):
        return obj.user_profile.user.username if obj.user_profile else None

    user_profile.short_description = 'User Profile'