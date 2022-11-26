from rest_framework.serializers import ModelSerializer
from .models import ResearchTable


class ResearchSerializer(ModelSerializer):
    class Meta:
        model = ResearchTable
        fields = "__all__"