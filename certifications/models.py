
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class certfication(models.Model):
    option=(("Not Completed","Not Completed"),("Completed","Completed"))
    event_name=models.CharField(max_length=50)
    mentor_name=models.CharField(max_length=25) 
    issue_date=models.DateField()
    img=models.ImageField(upload_to = "certificate")
    status=models.CharField(max_length=15,choices=option)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
class user_certificates(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    certificate=models.ForeignKey(certfication,on_delete=models.CASCADE,related_name='user_certs')
    # DELETE FROM public.django_migrations WHERE public.django_migrations.app = 'certifications';
    
    
    
