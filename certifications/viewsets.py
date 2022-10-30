from donate import serializers
from rest_framework import viewsets
from .models import certfication
from . import serilaizers

class CertificateViewset(viewsets.ModelViewSet):
    
    queryset=certfication.objects.all()
    serializer_class=serilaizers.certificationSerializer