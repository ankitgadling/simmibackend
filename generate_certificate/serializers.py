from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from certifications.models import certfication
from .models import DonationCetificates
from django.contrib.auth.models import User

class CertSerializer(ModelSerializer):
    class Meta:
        model = certfication
        fields = "__all__"
        
class Gen(serializers.Serializer):
    event_id = serializers.IntegerField()
    user_email = serializers.EmailField()



class GenarateDonationSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()
    email = serializers.EmailField()
    
    
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name',"last_name"]
    
    
class DonationDataSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = DonationCetificates
        fields = "__all__"
        