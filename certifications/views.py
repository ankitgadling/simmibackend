from urllib import request
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from .models import user_certificates,certfication
# from django.views.decorators import csrf_exempt
from rest_framework.response import Response
from .serilaizers import certificationSerializer, user_certificateSerializer,UserCertificateSerializer
#from accounts.models import registration
from rest_framework import status
from rest_framework.mixins import DestroyModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from .serilaizers import user_certificateSerializer,certificationSerializer

class genview(generics.ListCreateAPIView):
    queryset=certfication.objects.all()
    serializer_class=certificationSerializer
    

class userview(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = user_certificates.objects.all()
    serializer_class = user_certificateSerializer
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
    serializer_class = UserCertificateSerializer
    queryset = certfication.objects.all()
    
    def get(self,request):
        user_id = request.session['current_user']
        user = User.objects.get()
        crts = certfication.objects.filter(user=user)
        data = UserCertificateSerializer(crts).data
        return Response(data)
    
    
    