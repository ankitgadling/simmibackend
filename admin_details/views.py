from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .serializers import AdminSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.

class AdmimDetailsView(GenericAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    
    def get(self,request,*args,**kwargs):
        listadmins = []
        Admins = User.objects.filter(is_staff=True,is_superuser=False)    
        for admin in Admins:
            listadmins.append({"admin_id":admin.id,"name":str(admin.first_name)+" "+str(admin.last_name)})
        return Response(listadmins)
    def post(self,request):
        usesname = request.data['email']
        try:
            user = User.objects.get(username=usesname)
            user.is_staff = True
            user.save()
            return Response("Admin permission added to this user!!")
        except User.DoesNotExist:
            return Response("User not found",404)
    

class AdmimDetailsView2(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializer

    def get(self,request,pk=None,*args,**kwargs):
        try:
            admin = User.objects.get(id=pk,is_staff=True,is_superuser=False)    
            return Response({"admin_id":admin.id,"name":str(admin.first_name)+" "+str(admin.last_name)})
        except User.DoesNotExist:
            return Response({"msg":"Admin Not Found....!"},404)
    def delete(self,request,pk=None,*args,**kwargs):
        try:
            admin = User.objects.get(id=pk)
            admin.is_staff = False
            admin.save()    
            return Response("Admin removed..!")
        except User.DoesNotExist:
            return Response({"msg":"Admin permission removed to this user..!"})
    
        
        
        
        