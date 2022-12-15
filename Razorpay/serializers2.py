from rest_framework import serializers



class TransactionsSerializer(serializers.Serializer):
    id = serializers.CharField()
    user = serializers.CharField()
    amount = serializers.CharField()
    cause = serializers.CharField()
    
    
class SubscriptionSerializer(serializers.Serializer):
    id = serializers.CharField()
    plan_id = serializers.CharField()
    user = serializers.CharField()
    amount = serializers.CharField()
    period = serializers.CharField()
    cause = serializers.CharField()
    