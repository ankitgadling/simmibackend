from django.shortcuts import render
from user_transactions.models import user_transactions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer 
from django.contrib.auth.models import User

# Create your views here.

class Userserializer(ModelSerializer):
    name = "madhu"
    class Meta:
        model = User
        fields = ["first_name","last_name"]


class user_transactionserializer(ModelSerializer):
    user = Userserializer(read_only=True)
    class Meta:
        model = user_transactions
        fields = "__all__"
        

class admin_transactions_view(ListAPIView):
    queryset = user_transactions.objects.all()
    serializer_class = user_transactionserializer