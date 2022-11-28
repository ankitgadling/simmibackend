from django.shortcuts import render
from Razorpay.models import Transactions,Subscription
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer 
from django.contrib.auth.models import User
# Create your views here.

class Userserializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name"]



class TransactionSerializer(ModelSerializer):
    user = Userserializer(read_only=True)
    class Meta:
        model = Transactions
        fields = "__all__"
        

class admin_transactions_view(ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    
    
    
class Userserializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name"]



class SubscriptionSerializer(ModelSerializer):
    user = Userserializer(read_only=True)
    class Meta:
        model = Subscription
        fields = "__all__"
        

class admin_subscription_view(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer