from rest_framework import serializers
from .models import *
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"    

class ExtraImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = "__all__"