from rest_framework import serializers
from .models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d/%b/%y", read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Transactions
        fields = "__all__"

    def get_status(self, obj):
        return "Success" if obj.is_paid else "Failed"
