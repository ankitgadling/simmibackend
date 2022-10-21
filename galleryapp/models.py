from django.db import models
# Create your models here.

class education(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = "gallery/Education")
    content = models.TextField()
    

class livelihood(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = "gallery/Education")
    content = models.TextField()
    


class medical_camps(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = "gallery/Education")
    content = models.TextField()
    

class women_empowerment(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = "gallery/Education")
    content = models.TextField()
    