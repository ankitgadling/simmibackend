from types import CodeType
from django.contrib import admin
from .models import Contact,Resp
admin.site.register(Resp)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mail', 'phone']
