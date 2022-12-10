from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from about.serializers import *
from about.models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin


class Intiativeapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Our_initiatives.objects.all()
    serializer_class = Initiativeserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class Initiativesapidetail(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =Our_initiatives.objects.all()
    serializer_class = Initiativeserializers
    def get(self,request,*args,**kwargs):
     return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Campaignapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Our_campaigns.objects.all()
    serializer_class = Campaignserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class Campaignapidetail(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =Our_campaigns.objects.all()
    serializer_class = Campaignserializers
    def get(self,request,*args,**kwargs):
     return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)