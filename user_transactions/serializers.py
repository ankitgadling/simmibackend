from rest_framework.serializers import ModelSerializer 
from .models import user_transactions
from account.models import SimmiUser
class Userserializer(ModelSerializer):
    class Meta:
        model = SimmiUser
        fields = ["username"]

class user_transactionserializer(ModelSerializer):
    user = Userserializer(read_only=True)
    class Meta:
        model = user_transactions
        fields = "__all__"
        
