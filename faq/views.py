from django.shortcuts import render
from rest_framework.generics  import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,DestroyAPIView
from .models import *
from .serializer import *
# Create your views here.


class FaqView(ListCreateAPIView):
    serializer_class = FaqSerializer
    queryset = FAQ.objects.all()
    

class FaqViewDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = FaqSerializer
    queryset = FAQ.objects.all()


class popupuserapi(ListAPIView):
    serializer_class = popserializer
    queryset = Popup.objects.all()

class popcreateapi(ListCreateAPIView):
    serializer_class = popserializer
    queryset = Popup.objects.all()

class popupdateapi(RetrieveUpdateDestroyAPIView):
    serializer_class = popserializer
    queryset = Popup.objects.all()

