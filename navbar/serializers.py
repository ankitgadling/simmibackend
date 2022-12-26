from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import upImages

class navbarserializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = upImages