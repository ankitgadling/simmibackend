from http.client import LENGTH_REQUIRED
from django.db import models

# Create your models here.
class donate_form(models.Model):
    name=models.CharField(max_length=100)
    phn_no=models.CharField(max_length=20)
    pan_no=models.TextField()
    address=models.TextField()
    email=models.EmailField()
    amount=models.IntegerField()
    purpose=models.TextField()

STATUS=((0,'Card Payment'),(1,'Internet Banking'),(2,'UPI & E-Wallet'),(3,'Other Payment Methods'))

class payment_method(models.Model):
    pay_using=models.IntegerField(choices=STATUS,default=0)


class payment_details(models.Model):

    card_no=models.IntegerField()
    ccv=models.IntegerField()
    exp_date=models.DateField()


            


