from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Gallerytable(models.Model):
    options = [
        ('Education', 'EDUCATION'),
        ('HealthCare', 'HEALTHCARE'),
        ('Livelihood', 'LIVELIHOOD'),
        ('Women Empowerment', 'WOMEN EMPOWERMENT'),
        ('Others', 'OTHERS')
    ]
    title = models.CharField(max_length=50)
    admin = models.CharField(max_length=50,default="Test-Admin", blank=True)
    photo = models.ImageField(upload_to = "gallery", blank=True)
    photo2 = models.ImageField(upload_to = "gallery", blank=True, default=None)
    photo3 = models.ImageField(upload_to = "gallery", blank=True,default=None)
    date = models.DateField(default=timezone.now)
    content = models.TextField()
    category = models.CharField(max_length=50,choices=options)
    #","livelihood",

    def __str__(self):
        return self.title