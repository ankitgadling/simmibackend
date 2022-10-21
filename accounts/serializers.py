from pyexpat import model
from rest_framework import serializers
from accounts.models import registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class Registrationserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class logindetailserializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Username or Password")

class accountserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email']
