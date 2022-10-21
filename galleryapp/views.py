from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from galleryapp.models import *
from galleryapp.serializers import *
# Create your views here.

#education
class educationapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =education.objects.all()
    serializer_class = Educationserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class educationapidetail(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =education.objects.all()
    serializer_class = Educationserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


#livelihood
class livelihoodapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =livelihood.objects.all()
    serializer_class = livelihoodserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class livelihoodapidetail(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =livelihood.objects.all()
    serializer_class = livelihoodserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


#medical_camps
class medical_campsapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =medical_camps.objects.all()
    serializer_class = medical_campsserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class medical_campsapidetail(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =medical_camps.objects.all()
    serializer_class = medical_campsserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


#women_empowerment
class women_empowermentapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =women_empowerment.objects.all()
    serializer_class = women_empowermentserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class women_empowermentapidetail(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =women_empowerment.objects.all()
    serializer_class = women_empowermentserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)





