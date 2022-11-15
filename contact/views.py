from operator import truediv
from django.shortcuts import render
from .models import Contact,Resp
from rest_framework.response import Response
from .serializers import ContactSerializer,responseserializers
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin



@api_view(['POST', "GET"])
def contact(request):
    if request.method == "POST":
        try:
            data = request.data
            serializer = ContactSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Status": 200,
                    "data": serializer.data
                })
            return Response({
                    "Status": False,
                    "message": "Invalid data!",
                    "data": serializer.errors
                })

        except Exception as e:
            return Response({
                "status":"something went wrong"
            })
    if request.method == "GET":
        obj = Contact.objects.all()
        serializer = ContactSerializer(obj, many=True)
        return Response(serializer.data)


class responseapi(GenericAPIView,CreateModelMixin):
    queryset=Resp.objects.all()
    serializer_class=responseserializers    
    def post(self,request,*args,**kwargs):
        return self.create(self,request,*args,**kwargs)