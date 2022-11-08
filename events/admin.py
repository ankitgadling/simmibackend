from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Event)
admin.site.register(EventImages)

@admin.register(Speaker)
class Speaker(admin.ModelAdmin):
    list_display = ['speaker_name', 'event_name', 'place']
