from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from certifications.models import certfication

class CertSerializer(ModelSerializer):
    class Meta:
        model = certfication
        fields = "__all__"
        
class Gen(serializers.Serializer):
    event_id = serializers.IntegerField()
    user_email = serializers.EmailField()
