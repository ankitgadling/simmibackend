from unicodedata import category
from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import HybridImageField

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['category']

    
class BlogSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = Blog
        fields = '__all__'

    def to_representation(self, instance):
        category_name = super().to_representation(instance)
        category_name['category'] = CategorySerializer(instance.category).data
        return category_name
