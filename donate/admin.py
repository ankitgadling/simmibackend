from django.contrib import admin
from .models import donate_form, payment_details, payment_method, Give_Your_Help



class Admin_page_display(admin.ModelAdmin):
    list_display= ('name','email','phn_no')
    search_fields= ('name','email')

admin.site.register(donate_form,Admin_page_display)
admin.site.register(payment_method)
admin.site.register(payment_details)
admin.site.register(Give_Your_Help)