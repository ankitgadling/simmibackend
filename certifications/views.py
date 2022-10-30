from django.shortcuts import render

# from rest_framework import generics
from rest_framework.decorators import api_view
from .models import certfication
# from django.views.decorators import csrf_exempt
from rest_framework.response import Response
from .serilaizers import certificationSerializer
# Create your views here.

# class certficatelist(generics.ListCreateAPIView):
    
#     serializer_class=certificationSerializer
#     def get_queryset(self):
#         queryset=certfication.objects.all()
#         # user=


# @api_view(['GET','POST'])
# def certifcate_api(request):
#     if(request.method=='GET'):
#         cert_details=certfication.objects.all()
#         serilaizer=certificationSerializer(cert_details,many=True)
#         return Response(serilaizer.data)
#     if(request.method=="POST"):
#         data=request.data
#         serilaizer=certificationSerializer(data=data)
#         if serilaizer.is_valid():
#             serilaizer.save()
#             res={'msg':'Data has been created Successfully'}
#             return Response(res,status=HTTP_201_CREATED)