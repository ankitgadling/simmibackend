from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class CustomSessions(models.Model):
    key = models.CharField(max_length=50,primary_key=True,unique=True)
    value = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    
    

class DonationCetificates(models.Model):
    transactions_id = models.CharField(max_length=30,default="-")
    certificate = models.FileField(upload_to="donation/certificates")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class SubscriptionCetificates(models.Model):
    subscription_id = models.CharField(max_length=30)
    certificate = models.FileField(upload_to="donation/subscription/certificates")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    