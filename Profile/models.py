from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class UserInformation(models.Model):
    username = models.CharField(max_length=30, unique=True, default=None)
    profile = models.CharField(max_length=30, default=None)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, default=None)
    email = models.CharField(max_length=255, unique=True)

    dob = models.CharField(max_length=30, default=None)
    city = models.CharField(max_length=255, default=None)
    State = models.CharField(max_length=255, default=None)
    country = models.CharField(max_length=255, default=None)
    college = models.CharField(max_length=255, default=None)
    clg_email = models.CharField(max_length=255, unique=True, default=None)
    clg_city = models.CharField(max_length=255, default=None)

    failed_login_attempts = models.CharField(max_length=30, default=None)
    last_login = models.CharField(max_length=30, default=None)
    last_password_change = models.CharField(max_length=30, default=None)
    status = models.CharField(max_length=30, default=None)

    friends_phone_numbers = models.CharField(max_length=30, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_user_information(self, phone_number):
        """
        fetch the user information from the database.
        """


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargßs):
    if created:
        Token.objects.create(user=instance)
