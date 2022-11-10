from rest_framework import serializers
from .models import *
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"    

class EventSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['attendence']    
