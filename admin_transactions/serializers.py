from rest_framework.serializers import ModelSerializer 
from django.contrib.auth.models import User
from Razorpay.models import Transactions,Subscription
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


class SubscriptionSerializer(ModelSerializer):
    user = Userserializer(read_only=True)
    class Meta:
        model = Subscription
        fields = "__all__"
