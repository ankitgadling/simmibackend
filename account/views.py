from django.contrib.auth import authenticate
from django.http import JsonResponse ,HttpResponse
from .serializers import Registrationserializers,userdetails,logindetailserializers,accountserializer,userupdateserializer,userprofileupdateserializer,ChangePasswordSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from knox.views import LogoutView
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from account.models import SimmiUserDetails
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import DateTimeField
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import knox_settings

#import requests
#import json

from django.contrib.auth.hashers import check_password

# Create your views here.

class register_api(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = Registrationserializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"msg": "Registration Successfull...!"})


class userdetailsupdateview(generics.GenericAPIView):
    queryset = SimmiUserDetails.objects.all()
    serializer_class = userupdateserializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self,request,*args,**kwargs):
        first_name = request.data.get('first_name',None)
        last_name = request.data.get('last_name',None)
        ph_no = request.data.get('ph_no',None)
        profile = request.data.get('profile',None)
        email = request.user.username
        user = User.objects.get(username=email)
        userdetails = SimmiUserDetails.objects.get(user= user)
        if first_name is not None:
            userdetails.first_name = first_name
        if last_name is not None:
            userdetails.last_name = last_name
        if ph_no is not None:
            userdetails.ph_no = ph_no
        if profile is not None:
            userdetails.profile = profile
        userdetails.save()
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        user.save()
        return Response({"msg": "Update Successfull...!"})

class userprofileupdateview(generics.GenericAPIView):
    queryset = SimmiUserDetails.objects.all()
    serializer_class = userprofileupdateserializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self,request,*args,**kwargs):

        profile = request.data['profile']
        email = request.user.username
        user = User.objects.get(username=email)
        # pk = self.context.get('pk')
        user = SimmiUserDetails.objects.get(user=user)
        user.profile = profile
        user.save()
        return Response({"msg": "Profile updated...!"})




class Login_api(generics.GenericAPIView):
    serializer_class = logindetailserializers
    @csrf_exempt
    def post(self, request, format=None):
        username = request.data['email']
        password = request.data['password']
        user = authenticate(username = username , password = password)
        if user is not None and not user.is_staff:
            try:
                obj = SimmiUserDetails.objects.get(user=user)
            except SimmiUserDetails.DoesNotExist:
                obj = None
            token = AuthToken.objects.create(user)[1]
            obj = userdetails(obj)
            if obj.data['profile'] is not None:
                profile = "https://simmibackend.pythonanywhere.com"+obj.data['profile']
            else:
                profile = "https://cdn0.iconfinder.com/data/icons/user-pictures/100/unknown_1-2-512.png"
            obj ={
                'id':user.id,
                'email':user.username,
                'first_name':obj.data['first_name'],
                'last_name':obj.data['last_name'],
                'ph_no':obj.data['ph_no'],
                'profile':profile,
            }
            if obj['profile'] is None:
                 pass
            request.session['current_user'] = user.id
            print(request.session['current_user'])
            return Response({"msg": "Login Successfull...!","token":token,"user":accountserializer(user).data,"userdetals":obj })
        else:
            return Response({
                "msg": "User Not Found...!"
            },404)

class ChangePassword(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        confirm_password = request.data['confirm_password']
        email = request.user.username

        if confirm_password == new_password:
            user = User.objects.get(username=email)
            if check_password(old_password , user.password):
                user.set_password(new_password)
                user.save()
                return Response('Password Changed...')
            else:
                return Response('wrong old password..!',400)
        else:
            return Response('invalide confirm password..!',400)



class LogoutUser(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class =userdetails
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        try:
            del request.session['current_user']
        except KeyError:
            pass
        return Response("Logout Successful!",200)

class Userinfo(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class =userdetails
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        email = request.user.username
        user = User.objects.get(username=email)
        userinfo = SimmiUserDetails.objects.get(user=user)
        try:
            data = {
                'first_name':userinfo.first_name,
                'last_name':userinfo.last_name,
                'ph_no':userinfo.ph_no,
                'profile':"https://simmibackend.pythonanywhere.com"+userinfo.profile.url
                }
        except:
            data = {
            'first_name':userinfo.first_name,
            'last_name':userinfo.last_name,
            'ph_no':userinfo.ph_no,
            'profile':"https://cdn0.iconfinder.com/data/icons/user-pictures/100/unknown_1-2-512.png"
            }
        return Response(data,200)





