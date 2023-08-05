from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Profile

# Register your models here.

class AccountAdmin(UserAdmin):
    '''
    Customizing Django Admin panel
    '''
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'is_active')
    filter_horizontal = ()
    list_filter = ('is_admin', 'is_staff', 'is_active')
    # Grouping fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    )
    # Set as readonly
    readonly_fields = ('last_login', 'date_joined')
    # Order by date joined
    ordering = ('-date_joined',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'country')


admin.site.register(Account, AccountAdmin)
admin.site.register(Profile, ProfileAdmin)
