from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Transactions(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE, related_name='payments')
    amount = models.CharField(max_length=25)
    is_paid = models.BooleanField(default=False)
    cause = models.CharField(max_length=50, default='Simmi Foundation')
    date = models.DateTimeField(auto_now=True)