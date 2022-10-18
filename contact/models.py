from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()    

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
        