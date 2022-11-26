from django.db import models
from django.utils import timezone

# Create your models here.


class CustomSessions(models.Model):
    key = models.CharField(max_length=50,primary_key=True,unique=True)
    value = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    
    