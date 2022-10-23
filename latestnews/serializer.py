from rest_framework import serializers
from .models import LatestNews


class LatestNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LatestNews
        fields = '__all__'