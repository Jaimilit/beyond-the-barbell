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
    """Admin view of trainer reviews"""
    list_display = ['title', 'trainer', 'rating']
    search_fields = ['trainer', 'content']
    list_filter = ['trainer', 'rating']
    actions = ['delete_review']

    def delete_review(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected reviews were deleted.")

    delete_review.short_description = "Delete selected reviews"


