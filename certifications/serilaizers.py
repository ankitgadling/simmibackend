

# from rest_framework import serializers
# from .models import certfication,user_certificates
# from rest_framework.fields import SerializerMethodField 


        
# class certificationSerializer(serializers.ModelSerializer):
#     # users=user_certificateSerializer(many=True,read_only=True)
#     class Meta:
#         model=certfication
#         fields="__all__"

# class user_certificateSerializer(serializers.ModelSerializer):

#     certificates=certificationSerializer(many=True,read_only=True)
#     class Meta:
#         model=user_certificates
#         fields="__all__"

from rest_framework import serializers
from .models import certfication,user_certificates
from rest_framework.fields import SerializerMethodField 
from django.contrib.auth.models import User


        
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['username']
        


class certificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=certfication
        fields="__all__"



class user_certificateSerializer(serializers.ModelSerializer):
    user = userSerializer()
    certificate=certificationSerializer()
    class Meta:
        model=user_certificates
        fields="__all__"
        

class UserCertificateSerializer(serializers.Serializer):
    event_name=serializers.CharField(max_length=50)
    mentor_name=serializers.CharField(max_length=25) 
    issue_date=serializers.DateField()
    img=serializers.ImageField()
    status=serializers.CharField()
    
    
        