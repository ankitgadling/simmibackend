from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import alliance
from drf_extra_fields.fields import HybridImageField

class Allianceserializers(ModelSerializer):
    img=HybridImageField()
    class Meta:
        model = alliance
        fields = "__all__"  


class ShortAlliance(ModelSerializer):
    class Meta:
        model=alliance
        fields=['id','company_name','desc']
