from rest_framework.serializers import ModelSerializer
from gallery.models import *
from drf_extra_fields.fields import HybridImageField


class Galleryserializers(ModelSerializer):
    image = HybridImageField()
    

    class Meta:
        model = Gallerytable
        fields = '__all__'     

class AdminSerializer(ModelSerializer):
    image = HybridImageField()

    class Meta:
        model = Gallerytable
        exclude = ['admin'] 