from django.shortcuts import render

from institutional_aliance.serializers import Allianceserializers, ShortAlliance
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin




class Alliance(GenericAPIView,ListModelMixin):
    queryset =alliance.objects.all()
    serializer_class = ShortAlliance
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class DetailedAlliance(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =alliance.objects.all()
    serializer_class = Allianceserializers
    def get(self,request,*args,**kwargs):
     return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)