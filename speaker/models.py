from django.db import models

class Speaker(models.Model):
    name = models.CharField('Speaker name',max_length=50)
    event = models.CharField(max_length=50)
    time = models.CharField(max_length=10)
    date = models.DateField()
    place = models.CharField(max_length=50)
    speaker_profile = models.ImageField(upload_to='events/speaker_profile')


    def __str__(self):
        return self.name