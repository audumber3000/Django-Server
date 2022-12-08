from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class UserInfo(models.Model):
    username = models.CharField(max_length=30 , unique=True , default=None)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=255, unique=True)
    dob = models.CharField(max_length=30 , default=None)
    city = models.CharField(max_length=255 , default=None)
    State = models.CharField(max_length=255 , default=None)
    college = models.CharField(max_length=255 , default=None)
    clg_email = models.CharField(max_length=255, unique=True , default=None)
    clg_city = models.CharField(max_length=255 , default=None)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargßs):
    if created:
        Token.objects.create(user=instance)


