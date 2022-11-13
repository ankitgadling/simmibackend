from .models import *
from .serializer import *
from rest_framework import viewsets

class IndividualSupporterView(viewsets.ModelViewSet):
    queryset = IndividualSupporter.objects.all()
    serializer_class = IndividualSupporterSerializer

class PressMediaView(viewsets.ModelViewSet):
    queryset = PressMedia.objects.all()
    serializer_class = PressMediaSerializer


class ElectronicMediaView(viewsets.ModelViewSet):
    queryset = ElectronicMedia.objects.all()
    serializer_class = ElectronicMediaSerializer


class EminentPersonalityView(viewsets.ModelViewSet):
    queryset = EminentPersonality.objects.all()
    serializer_class = EminentPersonalitySerializer