from datetime import date
from django.db import models


choices = [
        ('Education', 'EDUCATION'),
        ('HealthCare', 'HEALTHCARE'),
        ('Livelihood', 'LIVELIHOOD'),
        ('Women Empowerment', 'WOMEN EMPOWERMENT'),
        ('Others', 'OTHERS')
    ]
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
    created_by=models.CharField(max_length=50,default='someone')

    def __str__(self) -> str:
        return self.title

class Quote(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='welfare/quotes', blank=True)
    category = models.CharField(max_length=20, choices=choices, default='Education')

    def __str__(self):
        return self.name

class Timeline(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    date = models.DateField(default=date.today())
    category = models.CharField(max_length=20, choices=choices, default='Education')

    def __str__(self):
        return self.title


class Story(models.Model):

    title = models.CharField(max_length=30)
    link = models.URLField(max_length=200, blank=True, null=True)
    issue_on = models.DateField(default=date.today())
    description = models.TextField()
    image = models.ImageField(upload_to='welfare/story-of-change', blank=True)
    category = models.CharField(max_length=20, choices=choices, default='Education')

    def __str__(self):
        return self.title


class OtherCause(models.Model):
    choices2 = [
        ('Drug Rehabilitation', 'Drug Rehabilitation'),
        ('Elder Healthcare', 'Elder Healthcare'),
        ('Environment Protection', 'Environment Protection'),
        ('Disaster Management', 'Disaster Management')
    ]
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='welfare/other-causes', blank=True)
    date = models.DateField(default=date.today())
    category = models.CharField(max_length=50, choices=choices2, default='Drug Rehabilitation')

    def __str__(self):
        return self.title