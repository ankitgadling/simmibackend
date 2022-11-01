from django.contrib import admin
from account.models import SimmiUser

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name','last_name','ph_no', 'is_admin')
admin.site.register(SimmiUser,UserModelAdmin)