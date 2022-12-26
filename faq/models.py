from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class FAQ(models.Model):
    quention = models.TextField(help_text="frequently asked question from user")
    answer = models.TextField(help_text="answer")


class Popup(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField()
    img=models.ImageField(upload_to="popup/")
    
class SpendingMoneyPercentage(models.Model):
    education = models.CharField(max_length=10)
    healthcare = models.CharField(max_length=10)
    livelyhood = models.CharField(max_length=10)
    women_empowerment = models.CharField(max_length=10)
    other = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)