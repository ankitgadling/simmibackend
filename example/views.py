from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .s import S
from .models import M
# Create your views here.



class V(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = S
    queryset = M.objects.all()
    