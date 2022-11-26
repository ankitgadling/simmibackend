from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ResearchSerializer
from .models import ResearchTable

# Create your views here.


class Researches(ListCreateAPIView):
    queryset = ResearchTable.objects.all()
    serializer_class = ResearchSerializer
    

class ResearchesDetail(RetrieveUpdateDestroyAPIView):
    queryset = ResearchTable.objects.all()
    serializer_class = ResearchSerializer
