from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import Base64ImageField


class SpeakerSerializer(serializers.ModelSerializer):
    speaker_profile = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Speaker
        fields = '__all__'