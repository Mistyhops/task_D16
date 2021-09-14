from django.db import models
from django.contrib.auth.models import AbstractUser

import sys

sys.path.append("..")


class CustomUser(AbstractUser):
    pass


class OneTimeCode(models.Model):
    """
        OneTime codes used to confirm email, clears every day at 00:00
    """
    time = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=64, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.time}'
