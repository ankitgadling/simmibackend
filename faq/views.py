from django.shortcuts import render
from rest_framework.generics  import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializer import *
# Create your views here.


class FaqView(ListCreateAPIView):
    serializer_class = FaqSerializer
    queryset = FAQ.objects.all()
    

class FaqViewDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = FaqSerializer
    queryset = FAQ.objects.all()
    