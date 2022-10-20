from django.db import models

# Create your models here.
class registration(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
