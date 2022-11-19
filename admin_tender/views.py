from django.shortcuts import render

# Create your views here.

from tender.serializers import tenderserializers
from tender.models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class admintenderapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =tender.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['status']
    serializer_class = tenderserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class tendermodificationapi(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset =tender.objects.all()
    serializer_class = tenderserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)