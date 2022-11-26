from .models import *
from .serializer import *
from rest_framework import viewsets, generics

class IndividualSupporterView(viewsets.ModelViewSet):
    queryset = IndividualSupporter.objects.all()
    serializer_class = IndividualSupporterSerializer


class PressMediaView(viewsets.ModelViewSet):
    queryset = PressMedia.objects.all()
    serializer_class = PressMediaSerializer


class ElectronicMediaView(viewsets.ModelViewSet):
    queryset = ElectronicMedia.objects.all()
    serializer_class = ElectronicMediaSerializer


# class EminentPersonalityView(viewsets.ModelViewSet):
#     queryset = EminentPersonality.objects.all()
#     serializer_class = EminentPersonalitySerializer

class EminentPersonalityView(generics.ListCreateAPIView):
    queryset = EminentPersonality.objects.all()
    serializer_class = EminentPersonalitySerializer

class EminentPersonalityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = EminentPersonality.objects.all()
    serializer_class = EminentPersonalitySerializer

class PublicationView(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class AwardsRecognitionView(viewsets.ModelViewSet):
    queryset = AwardsRecognition.objects.all()
    serializer_class = AwardsRecognitionSerializer


class StoryOfChangeView(viewsets.ModelViewSet):
    queryset = StoryOfChange.objects.all()
    serializer_class = StoryOfChangeSerializer
    
    
