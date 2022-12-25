from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import alliance,Coparate
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


class copartnerserializers(ModelSerializer):
    class Meta:
        model=Coparate
        fields="__all__"

class copatnershort(ModelSerializer):
    class Meta:
        model = Coparate
        fields = ['id','comp_name','partner_since','img','logo']
class copatnerlong(ModelSerializer):
    class Meta:
        model = Coparate
        fields = "__all__"