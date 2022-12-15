from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers2 import *
from account.models import SimmiUserDetails
from .models import Transactions,Subscription

class TransactionsView(GenericAPIView):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()
    
    def post(self,request):
        id = request.data['id']
        amount = request.data['amount']
        user_id = request.data['user']
        user = SimmiUserDetails.objects.get(id=int(user_id)).user
        cause = request.data['cause']
        trance = Transactions.objects.create(id=id,amount=amount,user=user,cause=cause)
        print(trance)
        return Response(trance)
    

class SubscriptionView(GenericAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    
    def post(self,request):
        id = request.data['id']
        plan_id = request.data['plan_id']
        amount = request.data['amount']
        period = request.data['period']
        user_id = request.data['user']
        user = SimmiUserDetails.objects.get(id=int(user_id)).user
        cause = request.data['cause']
        sub = Subscription.objects.create(id=id,plan_id=plan_id,amount=amount,user=user,cause=cause,period=period)
        print(sub)
        return Response(sub)
    
 