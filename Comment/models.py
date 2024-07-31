from django.utils.timezone import now
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

from Post.models import Post

# Create your models here.
class Comment(models.Model):
    # 使用ckeditor
    content = RichTextField(config_name='limited', max_length=300)
    created_time = models.DateTimeField('create_time', default=now)
    update_time = models.DateTimeField('modified_time', default=now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', verbose_name="parent_comment", blank=True, null=True, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        ordering = ['id']
        verbose_name = "Comment"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)