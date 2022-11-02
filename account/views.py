from django.contrib.auth import authenticate
from .serializers import Registrationserializers,userdetails,logindetailserializers,accountserializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from account.models import SimmiUserDetails
# Create your views here.

class register_api(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = Registrationserializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"msg": "Registration Successfull...!"})
    




class Login_api(generics.GenericAPIView):
    serializer_class = logindetailserializers
    @csrf_exempt
    def post(self, request, format=None):
        username = request.data['email']
        password = request.data['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            obj = SimmiUserDetails.objects.get(user=user)
            token = AuthToken.objects.create(user)[1]
            obj = userdetails(obj)
            obj ={
                'first_name':obj.data['first_name'],
                'last_name':obj.data['last_name'],
                'ph_no':obj.data['ph_no'],
                'profile':obj.data['profile'],
            }
            if obj['profile'] is None:
                 obj['profile'] = "https://cdn0.iconfinder.com/data/icons/user-pictures/100/unknown_1-2-512.png"
            return Response({"msg": "Login Successfull...1","token":token,"user":accountserializer(user).data,"userdetals":obj })
        else:
            return Response({
                "msg": "User Not Found...!"
            })


