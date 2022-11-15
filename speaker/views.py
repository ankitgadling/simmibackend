from .models import *
from .serializer import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response


class AllSpeakers(ListAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class PostSpeaker(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class CRUDSpeaker(RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
