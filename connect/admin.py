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
    search_fields = ['trainer', 'content']
    list_filter = ['trainer', 'rating', 'date_posted']
    actions = ['delete_review']

    def delete_review(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected reviews were deleted.")
        actions = ['approve_trainer_review']

    def approve_trainer_review(self, request, queryset):
        queryset.update(approved=True)

    # Customize the display name for the action
    delete_review.short_description = "Delete selected reviews"
