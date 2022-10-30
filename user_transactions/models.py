from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_transactions(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=20)
    amount = models.IntegerField(default=100)
    status = models.CharField(max_length=20,default="pending")
    