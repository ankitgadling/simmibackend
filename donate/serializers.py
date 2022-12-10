from dataclasses import fields
from rest_framework import serializers
from .models import Give_Your_Help, donate_form, payment_method,payment_details, upi_tran

class DonateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=donate_form
        fields="__all__"
        


class PaymentFormSerializers(serializers.ModelSerializer):
    class Meta:
        model=payment_method
        fields="__all__"



class Give_help_serializers(serializers.ModelSerializer):
    class Meta:
        model=Give_Your_Help
        fields="__all__"

class Upitranserializers(serializers.ModelSerializer):
    class Meta:
        model=upi_tran
        fields="__all__"

class PaymentShortserializer(serializers.ModelSerializer):
    class Meta:
        model=payment_details
        fields=['desc',"amount_type",'amount']
class PaymentDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=payment_details
        fields="__all__"