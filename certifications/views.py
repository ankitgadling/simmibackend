import email
from urllib import request
from django.shortcuts import render
from donate import serializers
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from .models import user_certificates,certfication
# from django.views.decorators import csrf_exempt
from rest_framework.response import Response
from .serilaizers import certificationSerializer, user_certificateSerializer,UserCertificateSerializer, userSerializer,certificationSerializer2
#from accounts.models import registration
from rest_framework import status
from rest_framework.mixins import DestroyModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveAPIView
from django.contrib.auth.models import User
from .serilaizers import user_certificateSerializer,certificationSerializer,certificationSerializer2

class genview(generics.ListCreateAPIView):
    queryset=certfication.objects.all()
    serializer_class=certificationSerializer
    

class userview(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = user_certificates.objects.all()
    serializer_class = user_certificateSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
 

class newviewapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = certfication.objects.all()
    serializer_class = certificationSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)




class uview(generics.GenericAPIView,ListModelMixin,CreateModelMixin):
    serializer_class = user_certificateSerializer
    def get_queryset(self):
      queryset = user_certificates.objects.filter(pk=self.kwargs['id'])
      return queryset
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) 
      
      
class CurrentUserCertificates(generics.GenericAPIView):
    queryset = certfication.objects.all()
    serializer_class = certificationSerializer2

    
    def get(self,request,email):
        try:
            user = User.objects.get(username=email)
        except:
            return Response({"You are not participated in any events"})
        
        crts = certfication.objects.filter(user=user)
        user_certificates_all = []
        for c in crts:
            certificate = None
            if c.status == "Completed":
                certificate = "https://simmibackend.pythonanywhere.com"+c.img.url
            obj = {
                'id':c.id,
                "event_name":c.event_name,
                "mentor_name":c.mentor_name,
                "issued_date":c.issue_date,
                "certificate":certificate,
                "status":c.status
            } 
            user_certificates_all.append(obj)
        return Response(user_certificates_all)
    
    
class certificate_base_id(RetrieveAPIView):
    serializer_class = certificationSerializer
    queryset = certfication.objects.all()