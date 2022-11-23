from django.db import models

# Create your models here.

class FAQ(models.Model):
    quention = models.TextField(help_text="frequently asked question from user")
    answer = models.TextField(help_text="answer")