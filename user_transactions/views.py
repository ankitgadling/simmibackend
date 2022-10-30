from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import user_transactionserializer
from .models import user_transactions
# Create your views here.

class user_transactionsview(ListAPIView):
    queryset = user_transactions.objects.all()
    serializer_class = user_transactionserializer
    