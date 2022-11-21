from rest_framework.serializers import ModelSerializer
from gallery.models import Gallerytable
from drf_extra_fields.fields import HybridImageField


class Galleryserializers(ModelSerializer):
    photo = HybridImageField()
    class Meta:
        model = Gallerytable
        fields = '__all__'     

class AdminSerializer(ModelSerializer):
    photo = HybridImageField()
    class Meta:
        model = Gallerytable
        exclude = ['admin'] 