from dataclasses import fields
from rest_framework import serializers
from .models import Give_Your_Help, donate_form, payment_method,payment_details

class DonateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=donate_form
        fields="__all__"
        def validate(self, validated_data):
            if validated_data.get('phn_no'):
                phone = validated_data.get('phn_no')
                if len(phone) < 10:
                    raise serializers.ValidationError("Length of phone-no can't be < 10")
            
            return validated_data


class PaymentFormSerializers(serializers.ModelSerializer):
    class Meta:
        model=payment_method
        fields="__all__"

class PaymentDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=payment_details
        fields="__all__"

class Give_help_serializers(serializers.ModelSerializer):
    class Meta:
        model=Give_Your_Help
        fields="__all__"