from rest_framework.serializers import ModelSerializer
from gallery.models import Gallerytable


class Galleryserializers(ModelSerializer):
    class Meta:
        model = Gallerytable
        fields = "__all__"        
