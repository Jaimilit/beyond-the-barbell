from django.contrib import admin
from .models import Contact


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