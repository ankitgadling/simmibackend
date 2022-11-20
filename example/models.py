from django.db import models

# Create your models here.

class M(models.Model):
    image = models.ImageField(upload_to="cc")
    image_2 = models.ImageField(upload_to="cc")