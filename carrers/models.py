import email
from pyexpat import model
from re import T
from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator

# Create your models here.

class Jobs(models.Model):
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50,default="Work from office")
    admin = models.CharField(max_length=50,default="Test Admin")
    location = models.CharField(max_length=50)
    immediate_supervisor = models.CharField(max_length=50)
    salary_range = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    posted_date = models.DateField(auto_now_add=True)
    skills_req = models.TextField(null=True)
    description = models.TextField(max_length=60000 ,default="")
    
    def __str__(self):
        return self.title

class jobappliedbyuse(models.Model):
    how_you_heared_us=models.TextField(null=True)
    jobid=models.IntegerField()
    country=models.CharField(max_length=40)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    adhar_no=models.CharField(max_length=12,validators=[MinLengthValidator(12),MaxLengthValidator(12)],null=True)
    applied_on=models.DateField(auto_now_add=True)
    address_lane=models.TextField(null=True)
    city=models.CharField(max_length=30,null=True)
    postal_code=models.CharField(max_length=30,null=True)
    email=models.EmailField()
    country_code=models.CharField(max_length=5)
    mobile_number=models.CharField(max_length=16,null=False)
    resume=models.FileField(upload_to='Jobs/Resume/')
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE) 