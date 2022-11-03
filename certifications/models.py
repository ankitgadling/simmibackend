
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class certfication(models.Model):
    option=(("Not Attended","Not Attended"),("Completed","Completed"))
    event_name=models.CharField(max_length=50)
    mentor_name=models.CharField(max_length=25) 
    issue_date=models.DateField(auto_now=True)
    img=models.ImageField(upload_to = "certificate")
    status=models.CharField(max_length=15,choices=option)
class user_certificates(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    certificate=models.ForeignKey(certfication,on_delete=models.CASCADE,related_name='user_certs')