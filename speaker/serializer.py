from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import HybridImageField


class SpeakerSerializer(serializers.ModelSerializer):
    speaker_profile = HybridImageField()
    class Meta:
        model = Speaker
        fields = '__all__'