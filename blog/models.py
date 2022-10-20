from distutils.command.upload import upload
from http.client import UnimplementedFileMode
from django.db import models
import PIL

class Category(models.Model):
    category = models.CharField(max_length=20)


    def __str__(self):
        return self.category


class Blog(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='media/')
    date_posted = models.DateField()

    def __str__(self) -> str:
        return self.title
