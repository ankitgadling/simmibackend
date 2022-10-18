from dataclasses import fields
from rest_framework import serializers
from .models import donate_form, payment_method,payment_details

class DonateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=donate_form
        fields="__all__"


class PaymentFormSerializers(serializers.ModelSerializer):
    class Meta:
        model=payment_method
        fields="__all__"

class PaymentDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=payment_details
        fields="__all__"