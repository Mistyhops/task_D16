from django.contrib import admin

from .models import Announcement, Reply, Category


admin.site.register(Announcement)
admin.site.register(Reply)
admin.site.register(Category)
