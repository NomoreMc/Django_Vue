from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class DefaultUser(AbstractUser):
    create_time = models.DateTimeField(default=now)
    last_mod_time = models.DateTimeField(default=now)
    source = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = "DefaultUser"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

        # DefaulUser 默认只有评论权限
        # permissions = [
        #     ("create_post", "Can create post"),
        #     ("create_diary", "Can create diary"),
        #     ("create_series", "Can create series"),
        #     ("create_comment", "Can create comment"),
        #     ("create_update_log", "Can create update log"),
        # ]