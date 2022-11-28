from django.contrib import admin
from .models import CustomSessions,DonationCetificates,SubscriptionCetificates
# Register your models here.
admin.site.register(CustomSessions)
admin.site.register(DonationCetificates)
admin.site.register(SubscriptionCetificates)