from rest_framework import serializers
from drf_extra_fields.fields import HybridImageField
from .models import *

class IndividualSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualSupporter
        fields = "__all__"

class PressMediaSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = PressMedia
        fields = '__all__'

class ElectronicMediaSerializer(serializers.ModelSerializer):
    picture = HybridImageField()
    class Meta:
        model = ElectronicMedia
        fields = '__all__'

class EminentPersonalitySerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = EminentPersonality
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = Publication
        fields = '__all__'


class AwardsRecognitionSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = AwardsRecognition
        fields = '__all__'

class StoryOfChangeSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = StoryOfChange
        fields = '__all__'