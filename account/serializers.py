from pyexpat import model
from rest_framework import serializers
#from accounts.models import registration
from .models import SimmiUser
from django.contrib.auth import authenticate

class Registrationserializers(serializers.ModelSerializer):
    class Meta:
        model = SimmiUser
        fields = ['first_name', 'last_name', 'ph_no','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
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
        model = SimmiUser
        fields = ['first_name', 'last_name', 'ph_no','email']
