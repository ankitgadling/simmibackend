from django.contrib.auth import authenticate
from account.models import SimmiUser
from .serializers import Registrationserializers, logindetailserializers, accountserializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from .models import SimmiUser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import user_profile
# Create your views here.

class register_api(generics.GenericAPIView):
    queryset = SimmiUser.objects.all()
    serializer_class = Registrationserializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response({"msg": "Registration Successfull...!"})
    




class Login_api(generics.GenericAPIView):
    serializer_class = logindetailserializers
    @csrf_exempt
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            try:
                obj = user_profile.objects.get(user=user)
                profile = obj.profile
            except user_profile.DoesNotExist:
                profile = 'https://cdn0.iconfinder.com/data/icons/user-pictures/100/unknown_1-2-512.png'
            token = AuthToken.objects.create(user)[1]
            return Response({"msg": "Login Successfull...1","token":token,"user":accountserializer(user).data,"profile":profile })
        else:
            return Response({
                "msg": "User Not Found...!"
            })


