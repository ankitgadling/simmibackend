from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Volunteer(models.Model):
    name=models.CharField(max_length=30,null=False)
    email=models.EmailField(null=False)
    phone=models.CharField(max_length=12,validators=[MinLengthValidator(10)],null=False)
    address=models.TextField(null=False)
    aadhar_no=models.CharField(max_length=16,validators=[MinLengthValidator(16)],null=False)
    dob=models.DateField(null=False)
    blood_group=models.CharField(max_length=10,null=False)