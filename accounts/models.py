from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Country(models.Model):
  name = models.CharField(max_length=50)
  abbr = models.CharField(max_length=5)
  is_active = models.BooleanField(default=True)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Country'
    verbose_name_plural = 'Countries'
    db_table = 'countries'


class Profile(models.Model):
  user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
  country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
  avatar = models.ImageField(blank=True, upload_to='profile_avatars/')


class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4

    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB, 'web'),
        (DEVICE_IOS, 'ios'),
        (DEVICE_ANDROID, 'android'),
        (DEVICE_PC, 'pc'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='devices', on_delete=models.CASCADE
    )
    device_uuid = models.UUIDField('Device UUID', null=True)
    last_login = models.DateTimeField('Last Login Date', null=True)
    device_type = models.PositiveSmallIntegerField(
        choices=DEVICE_TYPE_CHOICES, default=DEVICE_WEB
    )
    device_os = models.CharField('Device OS', max_length=20, blank=True)
    device_model = models.CharField('Device Model', max_length=50, blank=True)
    app_version = models.CharField('App Version', max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

