from django.db import models
from ckeditor.fields import RichTextField

from accounts.models import CustomUser

import sys

sys.path.append("..")


class Announcement(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    header = models.CharField(max_length=256)
    text = RichTextField()
    category = models.ManyToManyField('Category')

    def __str__(self):
        return f'{self.header}'

    def get_absolute_url(self):
        return f'/announcements/{self.pk}/'


class Reply(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=512)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.text}'


class Category(models.Model):
    name = models.CharField(max_length=64)
    subscriber = models.ManyToManyField(CustomUser, blank=True)

    def __str__(self):
        return f'{self.name}'
