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
    list_display = ['title', 'trainer', 'rating', 'date_posted', 'approved']
    search_fields = ['trainer', 'content']
    list_filter = ['trainer', 'rating', 'date_posted', 'approved']
    actions = ['delete_review', 'approve_reviews']

    def delete_review(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected reviews were deleted.")

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected reviews were approved and published.")

    delete_review.short_description = "Delete selected reviews"
    approve_reviews.short_description = "Approve selected reviews"
