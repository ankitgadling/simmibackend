from django.db import models

# Create your models here.
class alliance(models.Model):
    heading=models.CharField(max_length=25)
    company_name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='institutial_alliance/')
    desc=models.TextField()
    
    