from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import HybridImageField

class EventSerializer(serializers.ModelSerializer):
    image_1 = HybridImageField()
    image_2 = HybridImageField()
    image_3 = HybridImageField()
    class Meta:
        model = Event
        fields = "__all__"    

class EventSerializer2(serializers.ModelSerializer):
    image_1 = HybridImageField()
    image_2 = HybridImageField()
    image_3 = HybridImageField()
    class Meta:
        model = Event
        exclude = ['attendence']    
