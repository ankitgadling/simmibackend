from about.models import *
from rest_framework.serializers import ModelSerializer



class Initiativeserializers(ModelSerializer):
    class Meta:
        model = Our_initiatives
        fields = "__all__"  

class Campaignserializers(ModelSerializer):
    class Meta:
        model = Our_campaigns
        fields = "__all__"  