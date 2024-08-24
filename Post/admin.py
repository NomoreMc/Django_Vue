from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    exclude = (
        # 'image',
        'last_mod_time',
    )

    list_display = (
        'title',
        'author',
        'date_posted',
        'last_mod_time',
        'comment_status',
    )

# Register your models here.
admin.site.register(Post, PostAdmin)