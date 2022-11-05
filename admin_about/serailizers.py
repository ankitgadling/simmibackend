from about.models import *
from rest_framework.serializers import ModelSerializer


class Aboutserializers(ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"        


class Founderserializers(ModelSerializer):
    class Meta:
        model = Founders
        fields = "__all__"        


class Advisoryserializers(ModelSerializer):
    class Meta:
        model = Advisory_board
        fields = "__all__"        


class Seniormanagementserializers(ModelSerializer):
    class Meta:
        model = Senior_management_committee
        fields = "__all__"        


class Seniortechnicalserializers(ModelSerializer):
    class Meta:
        model = Senior_technical_committee
        fields = "__all__"        



class teamserializers(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"  

class Initiativeserializers(ModelSerializer):
    class Meta:
        model = Our_initiatives
        fields = "__all__"  

class Campaignserializers(ModelSerializer):
    class Meta:
        model = Our_campaigns
        fields = "__all__"  