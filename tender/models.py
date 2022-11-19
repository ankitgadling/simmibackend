from distutils.command.upload import upload
from secrets import choice
from django.db import models

# Create your models here.

class tender(models.Model):
    option=(
        ("Active","Active"),
        ("Archived","Archived")
    )
    tender_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="tender/")
    contents=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=10,choices=option)