from django.contrib import admin
from account.models import SimmiUserDetails

class UserModelAdmin(admin.ModelAdmin):
     list_display = ('user', 'first_name','last_name','ph_no' )
admin.site.register(SimmiUserDetails,UserModelAdmin)