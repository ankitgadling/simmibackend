from django.db import models
from account.models import SimmiUser
# Create your models here.

class user_transactions(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(SimmiUser, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=20)
    amount = models.IntegerField(default=100)
    status = models.CharField(max_length=20,default="pending")
    
