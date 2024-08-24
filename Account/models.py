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

# Profile Model
from django.core.files.storage import default_storage
from django.conf import settings
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{ self.user.username } Profile'

    def save(self, *arg, **kwargs):
        if self.pk:
            old_profile = Profile.objects.get(pk=self.pk).image
            if old_profile.name != self.image.name and old_profile.name != 'default.png':
                default_storage.delete(old_profile.path)
        super().save(*arg, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
