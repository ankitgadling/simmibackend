from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class donate_form(models.Model):
    name=models.CharField(max_length=100,null=False)
    phn_no=models.CharField(max_length=12,validators=[MinLengthValidator(10)],null=False)
    pan_no=models.IntegerField(validators=[MinLengthValidator(10),MaxLengthValidator(10)],null=False)
    address=models.TextField(null=False)
    date=models.DateField(auto_now=True,null=False)
    email=models.EmailField(null=False)
    user=user=models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.IntegerField(null=False)
    purpose=models.TextField(null=False)

STATUS=((0,'Card Payment'),(1,'Internet Banking'),(2,'UPI & E-Wallet'),(3,'Other Payment Methods'))

class payment_method(models.Model):
    pay_using=models.IntegerField(choices=STATUS,default=0)





class Give_Your_Help(models.Model):
    contents=models.TextField(null=False)

class upi_tran(models.Model):
    username=models.CharField(max_length=20,null=False)
    paas=models.CharField(max_length=35,validators=[MinLengthValidator(8)],null=False)




class payment_details(models.Model):
    options = [
        ("Education","Education"),
        ("Women Empowerment","Women Empowerment"),
        ("Livlihood","Livlihood"),
        ("HealthCare","HealthCare"),
        ("Other","Other")
    ]

    subscription_plan=models.CharField(max_length=100)
    cause_for_donation=models.CharField(choices=options,max_length=100)
    amount_type=models.CharField(max_length=100)
    amount=models.CharField(max_length=9999999)
    fname=models.CharField(max_length=25)
    email=models.EmailField()
    country_code=models.CharField(max_length=10)
    num=models.CharField(max_length=18)
    country=models.CharField(max_length=25)
    desc=models.TextField(null=True)

