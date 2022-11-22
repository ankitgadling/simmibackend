from django.shortcuts import render

from institutional_aliance.serializers import Allianceserializers, ShortAlliance, copartnerserializers
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


class AdminAlliance(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =alliance.objects.all()
    serializer_class = Allianceserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class AdmineditAlliance(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Copatner.objects.all()
    serializer_class=copartnerserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Copatnerapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Copatner.objects.all()
    serializer_class=copartnerserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)



class AdminCopatnerapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Copatner.objects.all()
    serializer_class=copartnerserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class AdmineditCopatnerapi(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Copatner.objects.all()
    serializer_class=copartnerserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)