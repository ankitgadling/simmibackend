from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import Adminloginserializer,ChangePasswordSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from account.models import SimmiUserDetails
from simmibackend.settings import SUPER_USER_KEY
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .custome_permissions import IsSuperAdminUser
from django.conf import settings
from django.core.mail import EmailMessage


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
                if profile is None:
                    profile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
            except SimmiUserDetails.DoesNotExist:
                profile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
            if admin.is_staff == True:
                refresh = RefreshToken.for_user(admin)
                if admin.is_superuser == True:
                    if super_user_key == SUPER_USER_KEY:
                        #html = """<h2 style="color:orange;font-size:50px;text-align: center">Super Admin</h2><h3 class='text-center text-danger'>Login Successful!</h3>"""
                        #email = EmailMessage("login",html,settings.EMAIL_HOST_USER,['bagammagarimadhu@gmail.com'])
                        #email.content_subtype = "html"
                        #res = email.send()
                        return Response({
                            "msg":"Login Successful...!",
                            "admin":admin.username,
                            "profile":profile,
                            "adminType":"SuperAdmin",
                            'refresh': str(refresh),
                            'access': str(refresh.access_token)})
                    else:
                        return Response("Invalid Key!!",403)
                    
                else:
                    return Response({"msg":"Login Successful...!",
                                     "admin":admin.username,
                                     "profile":profile,
                                     "adminType":"NormalAdmin",
                                     'refresh': str(refresh),
                                    'access': str(refresh.access_token)
                                     })
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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperAdminUser]
    
    def post(self,request):
        email = request.data['email']
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        confirm_password = request.data['confirm_password']
        if confirm_password == new_password:
            admin = User.objects.get(username=email)
            if check_password(old_password , admin.password):
                admin.set_password(new_password)
                admin.save()
                return Response('Password Changed...')
            else:
                return Response('wrong old password..!',400)    
        else:
            return Response('invalide confirm password..!',400)
        
