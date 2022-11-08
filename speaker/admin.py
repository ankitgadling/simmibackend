from django.contrib import admin
from .models import *


@admin.register(Speaker)
class Speaker(admin.ModelAdmin):
    list_display = ['name', 'event', 'place', 'date']