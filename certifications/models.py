from django.db import models

# Create your models here.
class certfication(models.Model):
    option=(("Not Attended","Not Attended"),("Completed","Completed"))

    event_name=models.CharField(max_length=50)
    mentor_name=models.CharField(max_length=25)
    issue_date=models.DateField(auto_now=True)
    img=models.ImageField(upload_to = "certificates")
    status=models.CharField(max_length=15,choices=option)