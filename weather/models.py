from django.db import models
from users.models import User


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    favorite = models.BooleanField(default=False)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
