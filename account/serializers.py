from pyexpat import model
from rest_framework import serializers
from account.models import SimmiUserDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Registrationserializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    ph_no = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    #email = EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(max_length=50)
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        username = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        ph_no = validated_data['ph_no']
        user = User.objects.create_user(username=username,password=password)
        userdetails = SimmiUserDetails.objects.create(user=user,first_name=first_name,last_name=last_name,ph_no=ph_no)
        return user


class userdetails(serializers.ModelSerializer):
    class Meta:
        model = SimmiUserDetails
        fields = "__all__"



class logindetailserializers(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

#     def create(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Incorrect Username or Password")

class accountserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
