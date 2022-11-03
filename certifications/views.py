from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from .models import user_certificates,certfication
# from django.views.decorators import csrf_exempt
from rest_framework.response import Response
from .serilaizers import certificationSerializer, user_certificateSerializer
#from accounts.models import registration
from rest_framework import status

from .serilaizers import user_certificateSerializer,certificationSerializer

class genview(generics.ListCreateAPIView):
    queryset=certfication.objects.all()
    serializer_class=certificationSerializer
    
class userview(generics.ListCreateAPIView):
    queryset=user_certificates.objects.all()
    serializer_class=user_certificateSerializer
