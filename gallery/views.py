from django.shortcuts import render
from gallery.serializers import Galleryserializers
from gallery.models import Gallerytable
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAdminUser

# get api for website without permissions
class Galleryapi(GenericAPIView,ListModelMixin):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
        
#for admins
class Galleryapidetail(RetrieveUpdateDestroyAPIView):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers
    permission_classes = [IsAdminUser]

    def get(self,request,*args,**kwargs):
     return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class GalleryAdmin(ListCreateAPIView):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers
    permission_classes = [IsAdminUser]

    def post(self,request, *args, **kwargs):
         return self.create(request, *args, **kwargs)