from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Statement)
admin.site.register(Week)
admin.site.register(WeekItemAssociation)