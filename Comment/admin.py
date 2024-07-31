from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    exclude = (
        'update_time',
    )

    list_display = (
        'author',
        'post',
        'created_time',
        'post',
        'parent_comment',
        'pk',
    )

# Register your models here.
admin.site.register(Comment, CommentAdmin)