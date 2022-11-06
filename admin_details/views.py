from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .serializers import AdminSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.

class AdmimDetailsView(ListAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    
    def get(self,request,*args,**kwargs):
        listadmins = []
        Admins = User.objects.filter(is_staff=True)    
        for admin in Admins:
            listadmins.append({"admin_id":admin.id,"name":str(admin.first_name)+" "+str(admin.last_name)})
        return Response(listadmins)
class AdmimDetailsView2(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializer

    def get(self,request,pk=None,*args,**kwargs):
        try:
            admin = User.objects.get(id=pk)    
            return Response({"admin_id":admin.id,"name":str(admin.first_name)+" "+str(admin.last_name)})
        except User.DoesNotExist:
            return Response({"msg":"Admin Not Found....!"})