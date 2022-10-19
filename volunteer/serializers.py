from .models import Volunteer
from rest_framework import serializers

class VolunteerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Volunteer
        fields="__all__"


