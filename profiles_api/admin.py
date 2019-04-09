from django.contrib import admin

from profiles_api import models


admin.site.register(models.UserProfile)
