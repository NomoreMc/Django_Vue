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

# Create your models here.
# class Topic(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

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
    image = models.ImageField(default='post_default.jpg', upload_to='post_images')
    # views = models.PositiveIntegerField(default=0)
    # tags = TaggableManager(blank=True)
    # topic = models.ManyToManyField(Topic, blank=True)
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

    # def viewed(self):
    #     self.views += 1
    #     self.save(update_fields=['views'])

    # 对上传的图片进行resize
    # def save(self, *args, **kwargs):
    #     is_update_views = isinstance(self, Post) and 'update_fields' in kwargs and kwargs['update_fields'] == ['views']
    #     if is_update_views:
    #         Post.objects.filter(pk=self.pk).update(views=self.views)
    #     else:
    #         if self.pk:
    #             old_image = Post.objects.get(pk=self.pk).image
    #             if old_image.name != self.image.name and old_image.name != 'post_default.jpg':
    #                 default_storage.delete(old_image.path)
    #         super().save(*args, **kwargs)

    #         img = Image.open(self.image.path)
    #         print("open image successfully")
    #         if img.width > 600:
    #             new_width = 600
    #             new_height = int(img.height * new_width / img.width)
    #             output_size = (new_width, new_height)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)

    def save(self, *args, **kwargs):
        # 如果是更新操作（而不仅仅是更新views字段），更新last_mod_time字段
        if self.pk and not ('update_fields' in kwargs and kwargs['update_fields'] == ['views']):
            self.last_mod_time = timezone.now()

        # 现有的保存逻辑
        is_update_views = isinstance(self, Post) and 'update_fields' in kwargs and kwargs['update_fields'] == ['views']
        if is_update_views:
            Post.objects.filter(pk=self.pk).update(views=self.views)
        else:
            if self.pk:
                old_image = Post.objects.get(pk=self.pk).image
                if old_image.name != self.image.name and old_image.name != 'post_default.jpg':
                    default_storage.delete(old_image.path)
            super().save(*args, **kwargs)

            img = Image.open(self.image.path)
            print("open image successfully")
            if img.width > 600:
                new_width = 600
                new_height = int(img.height * new_width / img.width)
                output_size = (new_width, new_height)
                img.thumbnail(output_size)
                img.save(self.image.path)