from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import *
from drf_extra_fields.fields import HybridImageField


class FaqSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class popserializer(ModelSerializer):
    img=HybridImageField()
    class Meta:
        model=Popup
        fields="__all__"