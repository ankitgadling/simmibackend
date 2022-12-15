from pyexpat import model
from rest_framework import serializers
from account.models import SimmiUserDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re

class Registrationserializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    ph_no = serializers.CharField()
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(max_length=50)
    confirm_password = serializers.CharField(max_length=50)
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        
        username = validated_data['email']
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        ph_no = validated_data['ph_no']
        
        #password validations
        if password != confirm_password:
            raise serializers.ValidationError('Password and Confirm Password are not matched....!')
        if len(password) < 8 :
            raise serializers.ValidationError('Password Must be atleast 8 characters....!')        
        if re.search('[0-9]',password) is None:
                raise serializers.ValidationError("Make sure your password has a number in it")
        if re.search('[A-Z]',password) is None: 
            raise serializers.ValidationError("Make sure your password has a capital letter in it")
        # names validations
#         if not str(first_name+last_name).isalpha():
#             raise serializers.ValidationError("Please use alphabets only for firstnname and lastname...!")
#         # phone number validation
        if not str(ph_no).isnumeric():
            raise serializers.ValidationError("Please Enter valide Phone Number...!")
        try:
            user = User.objects.get(username=username)
            raise serializers.ValidationError("Already used this email...!")
        except User.DoesNotExist: 
            user = User.objects.create_user(username=username,password=password ,first_name=first_name,last_name=last_name)
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


class userupdateserializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = SimmiUserDetails
        exclude = ['user','profile']
        
    def validate(self, attrs):
        first_name = attrs['first_name']
        last_name = attrs['last_name']
        ph_no = attrs['ph_no']
        email = attrs['email']
        # names validations
        if not str(first_name+last_name).isalpha():
            raise serializers.ValidationError("Please use alphabets only for firstname and lastname...!")
        # phone number validation
        if not str(ph_no).isnumeric():
            raise serializers.ValidationError("Please Enter valide Phone Number...!")
        return attrs
    
    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        ph_no = validated_data['ph_no']
        email = validated_data['email']
        user = User.objects.get(username=email)
        userdetails = SimmiUserDetails.objects.get(user= user)
        userdetails.first_name = first_name
        userdetails.last_name = last_name
        userdetails.ph_no = ph_no
        userdetails.save()
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return userdetails        
        
class userprofileupdateserializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = SimmiUserDetails
        fields = ['profile','email']
    
    def create(self, validated_data):
        profile = validated_data['profile']
        email = validated_data['email']
        user = User.objects.get(username=email)
        pk = self.context.get('pk')
        user = SimmiUserDetails.objects.get(user=user)
        user.profile = profile
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=None)
    new_password = serializers.CharField(max_length=None)
    confirm_password = serializers.CharField(max_length=None)
