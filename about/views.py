from django.shortcuts import render
from about.serializers import *
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin

# Create your views here.
class Aboutapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =About.objects.all()
    serializer_class = Aboutserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class Foundersapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Founders.objects.all()
    serializer_class = Founderserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class Advisorapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Advisory_board.objects.all()
    serializer_class = Advisoryserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class Seniormanagerapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Senior_management_committee.objects.all()
    serializer_class = Seniormanagementserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
        

class Seniortechapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Senior_technical_committee.objects.all()
    serializer_class = Seniortechnicalserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class Teamapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Team.objects.all()
    serializer_class = teamserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class Intiativeapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Our_initiatives.objects.all()
    serializer_class = Initiativeserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class Campaignapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =Our_campaigns.objects.all()
    serializer_class = Campaignserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)