from django.contrib import admin
from .models import *
# Register your models here.
class UpImagesAdmin(admin.ModelAdmin):
    list_display = ['img1','img2','img3','img4']
admin.site.register(upImages,UpImagesAdmin)
