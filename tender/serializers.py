from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import tender
from drf_extra_fields.fields import HybridImageField


class tenderserializers(ModelSerializer):
    img=HybridImageField()
    class Meta:
        model=tender
        fields="__all__"
