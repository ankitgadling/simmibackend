from rest_framework.serializers import ModelSerializer 
from .models import user_transactions
from django.contrib.auth.models import User
class Userserializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class user_transactionserializer(ModelSerializer):
    user = Userserializer(read_only=True)
    class Meta:
        model = user_transactions
        fields = "__all__"
        
