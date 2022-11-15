from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import Adminloginserializer,ChangePasswordSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from account.models import SimmiUserDetails
from simmibackend.settings import SUPER_USER_KEY
from django.contrib.auth.hashers import check_password

# Create your views here.

class admin_login(GenericAPIView):
    serializer_class = Adminloginserializer
    queryset = User.objects.all()
    
    def post(self,request,*args,**kwargs):
        username = request.data['email']
        password = request.data['password']
        super_user_key = request.data['key']
        
        admin = authenticate(username=username,password=password)
        
        if admin is not None:
            try:
                profile3 = SimmiUserDetails.objects.get(user=admin)
                profile = profile3.profile.url
            except SimmiUserDetails.DoesNotExist:
                profile = "https://res.cloudinary.com/dcc8pmavm/image/upload/v1/media/user%20profiles/admin_gdm3wb.jpg"
            if admin.is_staff == True:
                request.session['admin'] = admin.username
                if admin.is_superuser == True:
                    if super_user_key == SUPER_USER_KEY:
                        return Response({"msg":"Login Successful...!","admin":admin.username,"profile":profile,"adminType":"SuperAdmin"})
                    else:
                        return Response("Invalid Key!!")
                    
                else:
                    return Response({"msg":"Login Successful...!","admin":admin.username,"profile":profile,"adminType":"NormalAdmin"})
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

class ChangePassword(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    
    def post(self,request):
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        confirm_password = request.data['confirm_password']
        admin = request.session['admin']
        if confirm_password == new_password:
            admin = User.objects.get(username=admin)
            if check_password(old_password , admin.password):
                admin.set_password(new_password)
                admin.save()
                return Response('Password Changed...')
            else:
                return Response('wrong old password..!',400)    
        else:
            return Response('invalide confirm password..!',400)
        
