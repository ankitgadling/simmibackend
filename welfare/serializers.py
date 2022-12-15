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

    def to_representation(self, instance):
        category_name = super().to_representation(instance)
        category_name['category'] = CategorySerializer(instance.category).data
        return category_name


class QuoteSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = Quote
        fields = '__all__'


class TimelineSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%m/%Y',input_formats=None)

    class Meta:
        model = Timeline
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = Story
        fields = '__all__'
    

class OtherCauseSerializer(serializers.ModelSerializer):
    image = HybridImageField()
    class Meta:
        model = OtherCause
        fields = '__all__'