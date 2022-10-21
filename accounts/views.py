from django.contrib.auth import login
from accounts.models import registration
from .serializers import Registrationserializers, logindetailserializers, accountserializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
# Create your views here.


class register_api(generics.GenericAPIView):
    create_queryset = registration.objects.all()
    serializer_class = Registrationserializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response({"user": accountserializer(user, context=self.get_serializer_context()).data, 
    "token": token})


@api_view(["GET"])
def user(request):
    if request.method == "GET":
        obj = User.objects.all()
        serializer = accountserializer(obj, many=True)
        return Response(serializer.data)


class Login_api(generics.GenericAPIView):
    serializer_class = logindetailserializers

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({
                "status" : 200,
                "message" : "Logged in Successfully",
                "data" : serializer.data
            })

        else:
            return Response({
                "status": False,
                "message": "You are not a simmi admin"
            })


