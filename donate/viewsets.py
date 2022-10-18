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