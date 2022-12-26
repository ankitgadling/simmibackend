from distutils.command.upload import upload
from operator import truediv
from django.db import models

# Create your models here.
class upImages(models.Model):
    img1 = models.ImageField(null=False , upload_to = "navbar/images")
    img2 = models.ImageField(null=True, upload_to = "navbar/images")
    img3 = models.ImageField(null=True, upload_to = "navbar/images")
    img4 = models.ImageField(null=True, upload_to = "navbar/images")