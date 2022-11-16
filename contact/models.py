from distutils.command.upload import upload
from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator

class Resp(models.Model):
    name = models.CharField(max_length=25)
    num = models.CharField(max_length=10,validators=[MaxLengthValidator(10),MinLengthValidator(10)],null=False)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    message = models.TextField() 
    img=models.ImageField(upload_to="about/response_and_concern/") 

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

