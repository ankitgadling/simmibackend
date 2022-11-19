from django.shortcuts import render

from tender.serializers import tenderserializers
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class tenderapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =tender.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['status']
    serializer_class = tenderserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)