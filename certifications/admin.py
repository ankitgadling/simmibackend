from django.contrib import admin

from .models import certfication,user_certificates

# Register your models here.
admin.site.register(certfication)
admin.site.register(user_certificates)