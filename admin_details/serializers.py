
from rest_framework.serializers import Serializer,ModelSerializer
from django.contrib.auth.models import User
class AdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name',"last_name",'username']
        