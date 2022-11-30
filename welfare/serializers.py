from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import HybridImageField

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

    
class BlogSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = Blog
        fields = '__all__'