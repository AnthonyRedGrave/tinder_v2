from django.contrib import admin
from .models import Language, Profile, ProfileInformation
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe

admin.site.register(Profile)

admin.site.register(ProfileInformation)
admin.site.register(Language)
