from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from .admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings
from django.utils import timezone


class User(AbstractUser):


bio = models.TextField(blank=True)
profile_picture = models.ImageField(
    upload_to='profiles/', blank=True, null=True)
# Followers: who follows THIS user
followers = models.ManyToManyField(
    'self', symmetrical=False, related_name='following', blank=True
)


def __str__(self):


return self.username
