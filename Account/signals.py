# 信号
from django.db.models.signals import post_save
# 信源
from .models import DefaultUser, Profile
# 接收器
from django.dispatch import receiver

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

@receiver(post_save, sender=DefaultUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        # 赋予默认权限：默认只有 Comment 权限
        content_type = ContentType.objects.get_for_model(DefaultUser)
        permission = Permission.objects.get(
            codename='create_comment',
            content_type=content_type
        )
        user = get_object_or_404(DefaultUser, username=instance.username)
        user.user_permissions.add(permission)

@receiver(post_save, sender=DefaultUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()