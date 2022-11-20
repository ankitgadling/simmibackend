from rest_framework import serializers
from drf_extra_fields.fields import HybridImageField
from .models import *

class IndividualSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualSupporter
        fields = "__all__"

class PressMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressMedia
        fields = '__all__'

class ElectronicMediaSerializer(serializers.ModelSerializer):
    picture = HybridImageField()
    class Meta:
        model = ElectronicMedia
        fields = '__all__'

class EminentPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EminentPersonality
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = Publication
        fields = '__all__'