from django.contrib import admin
from .models import Contact
from .models import TrainerReview


class ContactAdmin(admin.ModelAdmin):
    """ View info from contact form in backend """
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'date',
    )


admin.site.register(Contact, ContactAdmin)


@admin.register(TrainerReview)
class TrainerReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'trainer', 'rating', 'date_posted']
    search_fields = ['title', 'content']
    list_filter = ['trainer', 'rating', 'date_posted']