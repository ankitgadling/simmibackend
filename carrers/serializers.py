from rest_framework.serializers import ModelSerializer
from carrers.models import Jobs
class Jobserializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"
        