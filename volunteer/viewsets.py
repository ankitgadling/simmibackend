from typing import ValuesView
from . import models
from . import serializers
from rest_framework import viewsets

class Volunteerviewsets(viewsets.ModelViewSet):
    
    queryset=models.Volunteer.objects.all()
    serializer_class=serializers.VolunteerSerializers