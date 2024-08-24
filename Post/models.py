from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from PIL import Image
# 标签
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.core.files.storage import default_storage

class Post(models.Model):
    COMMENT_STATUS = (
        ('o', 'open'),
        ('c', 'close'),
    )

    title = models.CharField(max_length=100)
    content = RichTextUploadingField(config_name='default')
    date_posted = models.DateTimeField(default=timezone.now)
    last_mod_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_status = models.CharField('comment status', max_length=1, choices=COMMENT_STATUS,default='o')


    def __str__(self):
        return self.title

    def comment_list(self):
        comments = self.comment_set.filter().order_by('-id')
        return comments

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk,
            })