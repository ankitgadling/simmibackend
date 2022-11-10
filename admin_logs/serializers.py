from rest_framework import serializers


class Adminloginserializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=None)
    key = serializers.CharField(max_length=None)