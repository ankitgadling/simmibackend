from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from carrers.models import Jobs, jobappliedbyuser
class Jobserializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"


class Job(ModelSerializer):
    class Meta:
        model = Jobs
        fields = ["department"]
        
class Jobapplyserializer(ModelSerializer):
    job = Job()
    class Meta:
        model=jobappliedbyuser
        fields="__all__"

class ShortJobapplyserializer(ModelSerializer):
    job=Job()
    
    class Meta:
        model=jobappliedbyuser
        fields=["first_name","applied_on","job"]



