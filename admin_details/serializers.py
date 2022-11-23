
from rest_framework.serializers import Serializer,ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
class AdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name',"last_name"]
        

class AdminAddSerializer(Serializer):
    email = serializers.EmailField()
