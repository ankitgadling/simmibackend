from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_description = models.TextField()
    speaker_name = models.CharField(max_length=50)
    Perk_of_attendig_event = models.TextField()
    category = models.CharField(max_length=50)
    time = models.CharField(max_length=30)
    image = models.ImageField(upload_to='events')
    date = models.DateField()
    attendence = models.IntegerField(default=0)
    place = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.event_name
    
class EventImages(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/extra_images')   


class Speaker(Event):
    speaker_profile = models.ImageField(upload_to='events/speaker_profile')
