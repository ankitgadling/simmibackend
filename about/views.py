from django.shortcuts import render
from about.serializers import *
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from django_filters.rest_framework import DjangoFilterBackend

# # Create your views here.
# class Aboutapi(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset =About.objects.all()
#     serializer_class = Aboutserializers
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class Foundersapi(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset =Founders.objects.all()
#     serializer_class = Founderserializers
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class Advisorapi(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset =Advisory_board.objects.all()
#     serializer_class = Advisoryserializers
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class Seniormanagerapi(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset =Senior_management_committee.objects.all()
#     serializer_class = Seniormanagementserializers
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
        

# class Seniortechapi(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset =Senior_technical_committee.objects.all()
#     serializer_class = Seniortechnicalserializers
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class Teamapi(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset =Team.objects.all()
#     serializer_class = teamserializers
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

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

class Createaboutapi(GenericAPIView,CreateModelMixin):
    queryset=commonAboutTable.objects.all()
    serializer_class=commonaboutserializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class Updateaboutapi(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset=commonAboutTable.objects.all()
    serializer_class=commonaboutserializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Viewaboutapi(GenericAPIView,ListModelMixin):
    queryset=commonAboutTable.objects.all()
    serializer_class=commonaboutserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['position']
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)