  
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms, models

admin.site.register(models.User)