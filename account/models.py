from django.db import models
from django.contrib.auth.models import User
#  Custom User Manager
class SimmiUserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)    
    ph_no = models.CharField(max_length=15)
    profile = models.ImageField(upload_to="user profiles/")
   
    