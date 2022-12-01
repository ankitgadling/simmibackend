from datetime import date
from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=20)


    def __str__(self):
        return self.category


class Blog(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='welfare/blogs')
    date_posted = models.DateField(default=date.today())

    def __str__(self) -> str:
        return self.title

class Quote(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='welfare/quotes', blank=True)

    def __str__(self):
        return self.name

class Timeline(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.title