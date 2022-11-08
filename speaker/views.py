from .models import *
from .serializer import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class AllSpeakers(ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class PostSpeaker(CreateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class CRUDSpeaker(RetrieveUpdateDestroyAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
