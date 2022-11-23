
from rest_framework.serializers import Serializer,ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
class AdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name',"last_name"]
        

class AdminAddSerializer(Serializer):
    email = serializers.EmailField()


class EmailSendSerializer(Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField(style={'base_template': 'textarea.html'})
    file = serializers.FileField()
    
