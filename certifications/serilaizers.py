from dataclasses import fields

from rest_framework import serializers
from .models import certfication


class certificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=certfication
        fields="__all__"