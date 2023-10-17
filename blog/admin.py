from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Post)
admin.site.register(models.Recipe)
admin.site.register(models.Comment)
