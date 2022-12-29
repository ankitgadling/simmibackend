from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import Adminloginserializer,ChangePasswordSerializer,UpdateSerializer
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
                profile = "https://simmibackend.pythonanywhere.com"+profile3.profile.url
                if profile is None:
                    profile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
            except SimmiUserDetails.DoesNotExist:
                profile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
            except ValueError:
                profile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
            if admin.is_staff == True:
                refresh = RefreshToken.for_user(admin)
                if admin.is_superuser == True:
                    if super_user_key == SUPER_USER_KEY:
                        # html = """<h2 style="color:orange;font-size:50px;text-align: center">Super Admin</h2><h3 class='text-center text-danger'>Login Successful!</h3>"""
                        # email = EmailMessage("login",html,settings.EMAIL_HOST_USER,['bagammagarimadhu@gmail.com'])
                        # email.content_subtype = "html"
                        # res = email.send()
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
    permission_classes = [IsAdminUser]
    
    def get(self,request):
        return Response(request.user.username)
    
    
    
    def post(self,request):
        email = request.user.username
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
        


class ProfileUpdate(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self,request):
        email = "madhu"#request.user.username
        user = User.objects.get(username=email)
        name = user.first_name
        try:
            profile = "https://simmibackend.pythonanywhere.com"+SimmiUserDetails.objects.get(user=user).profile.url
            if profile is None or len(profile) < 1 :
                profile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
        except:
            profile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
        return Response({'name':name,"profile":profile})    


    def put(self,request):
        email = request.user.username
        name = request.data.get('name',None)
        img = request.data.get('img',None)
        print(img)
        user = User.objects.get(username=email)
        if name is not None:
            user.first_name = name
        try:
            user2 = SimmiUserDetails.objects.get(user=user)
            if name is not None:
                user2.first_name = name
            if img is not None:
                user2.profile = img
        except SimmiUserDetails.DoesNotExist:
            user2 = SimmiUserDetails.objects.create(user=user,first_name=name,last_name="",ph_no="",profile=img)
        user.save()
        user2.save()
        
        return Response("updated....!")
    
    
