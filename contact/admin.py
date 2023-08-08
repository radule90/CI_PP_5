from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['is_answered', 'full_name', 'email', 'subject',
                    'created_at']
    search_fields = ['full_name', 'email', 'subject', 'message']
    list_display_links = ('is_answered', 'full_name', 'email',)
    list_filter = ('is_answered',)
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)
