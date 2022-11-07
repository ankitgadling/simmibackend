from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import Adminloginserializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from account.models import SimmiUserDetails
# Create your views here.

class admin_login(GenericAPIView):
    serializer_class = Adminloginserializer
    queryset = User.objects.all()
    
    def post(self,request,*args,**kwargs):
        username = request.data['email']
        password = request.data['password']
        
        admin = authenticate(username=username,password=password)
        
        if admin is not None:
            # try:
            #     profile = SimmiUserDetails.objects.get(user=admin)
            #     profile = "https://res.cloudinary.com/dcc8pmavm/image/upload/v1/"+str(profile.profile)+".png"
            # except SimmiUserDetails.DoesNotExist:
            profile = "https://res.cloudinary.com/dcc8pmavm/image/upload/v1/media/user%20profiles/admin_gdm3wb.jpg"
            if admin.is_staff == True:
                request.session['admin'] = admin.username
                if admin.is_superuser == True:
                    return Response({"msg":"Login Successful...!","admin":admin.username,"profile":profile,"admin-type":"Super-admin"})
                else:
                    return Response({"msg":"Login Successful...!","admin":admin.username,"profile":profile,"admin-type":"Normal-admin"})
            else:
                return Response("This user is not an admin...!",404)
        else:
            return Response('Admin not found...!',404)
    
class admin_logout(GenericAPIView):
    serializer_class = Adminloginserializer
    queryset = User.objects.all()
    
    def post(self,request,*args,**kwargs):
        try:
            del request.session['admin']
        except KeyError:
            pass
        return Response({"msg":"Logout Successful...!"}) 
                