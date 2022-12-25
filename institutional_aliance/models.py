
from django.db import models
from datetime import datetime
# Create your models here.
class alliance(models.Model):
    heading=models.CharField(max_length=25)
    company_name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='institutial_alliance/')
    desc=models.TextField()
    
class Coparate(models.Model):
    comp_name=models.CharField(max_length=25)
    patner_since = models.DateField(default=datetime.now)
    profession = models.CharField(max_length=25)
    img=models.ImageField(upload_to='Coparate_partnership/')
    desc=models.TextField()
    logo = models.ImageField(null=True)
    other_img = models.ImageField(null=True)

