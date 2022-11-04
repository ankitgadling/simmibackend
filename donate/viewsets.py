from rest_framework import viewsets
from . import models
from . import serializers

class DonateViewset(viewsets.ModelViewSet):
    
    queryset=models.donate_form.objects.all()
    serializer_class=serializers.DonateFormSerializer

class PaymentViewset(viewsets.ModelViewSet):
    
    queryset=models.payment_method.objects.all()
    serializer_class=serializers.PaymentFormSerializers

class PaymentDetailViewset(viewsets.ModelViewSet):
    
    queryset=models.payment_details.objects.all()
    serializer_class=serializers.PaymentDetailSerializers

class Give_help_Viewset(viewsets.ModelViewSet):
    
    queryset=models.Give_Your_Help.objects.all()
    serializer_class=serializers.Give_help_serializers


class Upi_viewset(viewsets.ModelViewSet):
    
    queryset=models.upi_tran.objects.all()
    serializer_class=serializers.Upitranserializers