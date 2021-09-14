from django.contrib import admin

from .models import CustomUser, OneTimeCode


admin.site.register(CustomUser)
admin.site.register(OneTimeCode)
