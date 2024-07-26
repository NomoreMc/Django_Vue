from django.contrib import admin

# Register your models here.
from .models import DefaultUser

class DefaultUserAdmin(admin.ModelAdmin):
    exclude = (
        'last_mod_time',
    )

    list_display = (
        'username',
        'source',
        'create_time',
        'is_active',
        'is_staff',
        'is_superuser',
    )

admin.site.register(DefaultUser, DefaultUserAdmin)