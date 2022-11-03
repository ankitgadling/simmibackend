from django.shortcuts import render
from gallery.serializers import Galleryserializers
from gallery.models import Gallerytable
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin

# Create your views here.
class Galleryapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class Galleryapidetail(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers
    def get(self,request,*args,**kwargs):
     return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

