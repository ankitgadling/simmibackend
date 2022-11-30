from django.shortcuts import render
from Razorpay.models import Transactions,Subscription
from rest_framework.generics import ListAPIView,GenericAPIView
from rest_framework.response import Response
from .serializers import Userserializer,TransactionSerializer,SubscriptionSerializer
from wsgiref.util import FileWrapper

class admin_transactions_view(ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
        
class admin_subscription_view(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    
    
class Donwnload_Donations(GenericAPIView):
    serializer_class= TransactionSerializer
    queryset = Transactions.objects.all()
    
    def get(self,request):
        date_list = []
        cause_list = []
        donation_id_list = []
        ammount_list = []
        action_list = []
        data = {
            "date":date_list,
            "cause":cause_list,
            "donation_id":donation_id_list,
            "ammount":ammount_list,
            "action":action_list
        }
        for i in self.get_queryset():
            if i.is_paid:
                action = "Donated"
            else:
                action = "Not Donated"
            date_list.append(i.date)
            cause_list.append(i.cause)
            donation_id_list.append(i.id)
            ammount_list.append(i.amount)
            action_list.append(action)
        return None