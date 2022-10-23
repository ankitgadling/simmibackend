from django.contrib import admin
from .models import LatestNews

@admin.register(LatestNews)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['headline', 'author', 'posted_date']
