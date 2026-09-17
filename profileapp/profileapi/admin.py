from django.contrib import admin
from profileapi import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)

