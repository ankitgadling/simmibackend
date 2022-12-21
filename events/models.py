from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_description = models.TextField()
    speaker_name = models.CharField(max_length=50)
    Perk_of_attendig_event = models.TextField()
    category = models.CharField(max_length=50)
    venue = models.CharField(max_length=50,blank=True,default="Online")
    online_link = models.CharField(max_length=300,blank=True,default="None")
    time = models.DateTimeField()
    image_1 = models.ImageField(upload_to='events',blank=True)
    # image_2 = models.ImageField(upload_to='events',blank=True)
    # image_3 = models.ImageField(upload_to='events',blank=True)
    duration = models.IntegerField(default=0)
    attendence = models.IntegerField(default=0)
    place = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.event_name
