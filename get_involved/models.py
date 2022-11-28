from datetime import date
from django.db import models
from django.utils import timezone

class IndividualSupporter(models.Model):
    name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    reason = models.TextField()
    timing = models.DateField()
    message = models.TextField()
    file = models.FileField(upload_to='supporter', blank=True)

    def __str__(self):
        return self.name    

class PressMedia(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='press_media', blank=True)

    def __str__(self):
        return self.name


class ElectronicMedia(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    picture = models.ImageField(upload_to='electronic_media',blank=True)

    def __str__(self):
        return self.title


class EminentPersonality(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to= 'eminent_personality', blank=True)
    company_name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField("News Paper",max_length=30)
    topic = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to = "publication", blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name


class AwardsRecognition(models.Model):
    recognition_from = models.CharField(max_length=100)
    recognition_by = models.CharField(max_length=100)
    description = models.TextField()
    issue_on = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to = 'awards and recognition', blank=True)

    def __str__(self):
        return self.recognition_from


class StoryOfChange(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    syndrome = models.CharField(max_length=255)
    how_we_helped = models.TextField()
    year = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to = 'story of change', blank=True)

    def __str__(self):
        return self.name

    def year_published(self):
        return self.year.strftime('%Y')