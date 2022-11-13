from django.db import models

class PressMedia(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()

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

    def __str__(self):
        return self.name