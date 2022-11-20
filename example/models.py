from django.db import models

# Create your models here.

class M(models.Model):
    image = models.ImageField(upload_to="cc")
    