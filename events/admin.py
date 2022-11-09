from django.contrib import admin
from .models import *
# Register your models here.
class GG(admin.ModelAdmin):
    list_display = ['event_name','time']
admin.site.register(Event,GG)


