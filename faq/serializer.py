from rest_framework.serializers import ModelSerializer
from .models import *

class FaqSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"