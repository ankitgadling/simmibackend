
from rest_framework.serializers import ModelSerializer
from .models import Advisory_board,Team,Senior_technical_committee,About,Founders,Senior_management_committee,Our_initiatives,Our_campaigns
from drf_extra_fields.fields import HybridImageField
class Aboutserializers(ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"        


class Founderserializers(ModelSerializer):
    img=HybridImageField()
    class Meta:
        model = Founders
        fields = "__all__"        


class Advisoryserializers(ModelSerializer):
    img=HybridImageField()
    class Meta:
        model = Advisory_board
        fields = "__all__"        


class Seniormanagementserializers(ModelSerializer):
    img=HybridImageField()
    class Meta:
        model = Senior_management_committee
        fields = "__all__"        


class Seniortechnicalserializers(ModelSerializer):
    img=HybridImageField()
    class Meta:
        model = Senior_technical_committee
        fields = "__all__"        



class teamserializers(ModelSerializer):
    img=HybridImageField()
    class Meta:
        model = Team
        fields = "__all__"  

class Initiativeserializers(ModelSerializer):
    photo=HybridImageField()
    class Meta:
        model = Our_initiatives
        fields = "__all__"  

class Campaignserializers(ModelSerializer):
    photo=HybridImageField()
    class Meta:
        model = Our_campaigns
        fields = "__all__"  