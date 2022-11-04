from django.core.validators import MaxLengthValidator,MinLengthValidator
from pyexpat import model
from django.db import models
# Create your models here.
class donate_form(models.Model):
    name=models.CharField(max_length=100,null=False)
    phn_no=models.CharField(max_length=12,validators=[MinLengthValidator(10)],null=False)
    pan_no=models.IntegerField(validators=[MinLengthValidator(10),MaxLengthValidator(10)],null=False)
    address=models.TextField(null=False)
    email=models.EmailField(null=False)
    amount=models.IntegerField(null=False)
    purpose=models.TextField(null=False)

STATUS=((0,'Card Payment'),(1,'Internet Banking'),(2,'UPI & E-Wallet'),(3,'Other Payment Methods'))

class payment_method(models.Model):
    pay_using=models.IntegerField(choices=STATUS,default=0)


class payment_details(models.Model):

    card_no=models.IntegerField(validators=[MinLengthValidator(16),MaxLengthValidator(16)],null=False)
    ccv=models.IntegerField(validators=[MinLengthValidator(3),MaxLengthValidator(3)])
    exp_date=models.DateField(null=False)


class Give_Your_Help(models.Model):
    contents=models.TextField(null=False)

class upi_tran(models.Model):
    username=models.CharField(max_length=20,null=False)
    paas=models.CharField(max_length=35,validators=[MinLengthValidator(8)],null=False)




