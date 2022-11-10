from django.contrib.auth import authenticate
from .serializers import Registrationserializers,userdetails,logindetailserializers,accountserializer,userupdateserializer,userprofileupdateserializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from account.models import SimmiUserDetails
from rest_framework.views import APIView
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

    def put(self,request,pk=None,*args,**kwargs):
        context = {"pk":pk}
        serializer = self.get_serializer(data=request.data,context=context)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"msg": "Update Successfull...!"})

class userprofileupdateview(generics.GenericAPIView):
    queryset = SimmiUserDetails.objects.all()
    serializer_class = userprofileupdateserializer

    def put(self,request,pk=None,*args,**kwargs):
        context = {"pk":pk}
        serializer = self.get_serializer(data=request.data,context=context)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"msg": "Profile updated...!"})




class Login_api(generics.GenericAPIView):
    serializer_class = logindetailserializers
    @csrf_exempt
    def post(self, request, format=None):
        username = request.data['email']
        password = request.data['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            try:
                obj = SimmiUserDetails.objects.get(user=user)
            except SimmiUserDetails.DoesNotExist:
                obj = None
            token = AuthToken.objects.create(user)[1]
            obj = userdetails(obj)
            obj ={
                'id':obj.data['id'],
                'first_name':obj.data['first_name'],
                'last_name':obj.data['last_name'],
                'ph_no':obj.data['ph_no'],
                'profile':obj.data['profile'],
            }
            if obj['profile'] is None:
                 obj['profile'] = "https://cdn0.iconfinder.com/data/icons/user-pictures/100/unknown_1-2-512.png"
            return Response({"msg": "Login Successfull...!","token":token,"user":accountserializer(user).data,"userdetals":obj })
        else:
            return Response({
                "msg": "User Not Found...!"
            })



# class LogoutView(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, format=None):
#         request._auth.delete()
#         user_logged_out.send(sender=request.user.__class__,
#                              request=request, user=request.user)
#         #user = User.objects.get()
#         logout(request,user)
#         return Response(None, status=status.HTTP_204_NO_CONTENT)
