
from rest_framework.serializers import ModelSerializer
from drf_extra_fields.fields import HybridImageField
from .models import M
class S(ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = M
        fields = "__all__"
        