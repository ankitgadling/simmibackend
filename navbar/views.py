from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from .models import upImages
from .serializers import navbarserializer
from rest_framework import permissions

# Create your views here.



class navbarupdateAPI(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = upImages.objects.all()
    serializer_class = navbarserializer
    permission_classes = (permissions.AllowAny,)
    def put(self, request, *args, **kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)