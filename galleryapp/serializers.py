from rest_framework.serializers import ModelSerializer
from galleryapp.models import *


class Educationserializers(ModelSerializer):
    class Meta:
        model = education
        fields = "__all__"
        
class livelihoodserializers(ModelSerializer):
    class Meta:
        model = livelihood
        fields = "__all__"
        
class medical_campsserializers(ModelSerializer):
    class Meta:
        model = medical_camps
        fields = "__all__"
        
class women_empowermentserializers(ModelSerializer):
    class Meta:
        model = women_empowerment
        fields = "__all__"
        