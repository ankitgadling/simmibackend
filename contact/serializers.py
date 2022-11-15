from rest_framework import serializers
from .models import Contact, Resp
from drf_extra_fields.fields import HybridImageField

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

    # def validate(self, validated_data):
    #     if validated_data.get('phone'):
    #         phone = validated_data.get('phone')
    #         if len(phone) < 10:
    #             raise serializers.ValidationError("Length of phone-no can't be < 10")
        
    #     return validated_data

class responseserializers(serializers.ModelSerializer):
    img=HybridImageField()
    class Meta:
        model=Resp
        fields="__all__"