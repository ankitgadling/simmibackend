from django.db import models

# Create your models here.

class Jobs(models.Model):
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    immediate_supervisor = models.CharField(max_length=50)
    salary_range = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    posted_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=60000 ,default="")
    
    def __str__(self):
        return self.title
    