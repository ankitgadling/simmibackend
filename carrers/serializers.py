from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from carrers.models import Jobs, jobappliedbyuse
from rest_framework import serializers
class Jobserializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"


class Job(ModelSerializer):
    class Meta:
        model = Jobs
        fields = ["department"]
        
class Jobapplyserializer(ModelSerializer):
    job = Jobserializer()
    class Meta:
        model=jobappliedbyuse
        fields="__all__"

class ShortJobapplyserializer(ModelSerializer):
    job=Job()
    
    class Meta:
        model=jobappliedbyuse
        fields=["id","first_name","applied_on","job"]

class newjobapplyserializer(serializers.Serializer):
    how_you_heared_us=serializers.CharField() 
    jobid=serializers.IntegerField() 
    country=serializers.CharField() 
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    adhar_no=serializers.CharField()
    applied_on=serializers.DateField()
    address_lane=serializers.CharField()
    city= serializers.CharField()
    postal_code=serializers.CharField()
    email=  serializers.EmailField()
    country_code=serializers.CharField()
    mobile_number=serializers.CharField()
    jobid=serializers.IntegerField()
    resume=serializers.FileField()

