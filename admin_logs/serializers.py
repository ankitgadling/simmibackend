from rest_framework import serializers


class Adminloginserializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=None)
    key = serializers.CharField(max_length=None)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=None)
    new_password = serializers.CharField(max_length=None)
    confirm_password = serializers.CharField(max_length=None)
    
    
    
