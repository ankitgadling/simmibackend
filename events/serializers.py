from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import HybridImageField

class EventSerializer(serializers.ModelSerializer):
    online_link = serializers.URLField(allow_blank=True)
    image_1 = HybridImageField()
    class Meta:
        model = Event
        fields = "__all__"    

class EventSerializer2(serializers.ModelSerializer):
    online_link = serializers.URLField(allow_blank=True)
    image_1 = HybridImageField()
    class Meta:
        model = Event
        exclude = ['attendence']    
