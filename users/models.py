from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField("Фото", upload_to=r"users/%Y/%m/%d/", blank=True, null=True)
