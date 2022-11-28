from django.contrib import admin
from .models import Transactions,Subscription
# Register your models here.
admin.site.register(Transactions)

class Subs(admin.ModelAdmin):
    list_display = ["id","user","amount","period"]
admin.site.register(Subscription,Subs)
