from rest_framework.generics import ListCreateAPIView, GenericAPIView, DestroyAPIView
from rest_framework.response import Response
from .serializers import Transactions, TransactionSerializer, Subscription, SubscriptionSerializer
import json
from .razorpay_client import RazorpayClient
# Create your views here.


class TransactionAPIView(ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        if self.request.data.get('subscription') == 'true':
            return Subscription.objects.all()

        return self.queryset

    def get_serializer_class(self):
        if self.request.data.get('subscription') == 'true':
            return SubscriptionSerializer

        return self.serializer_class

    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        subscription = True if request.data.get(
            'subscription') == 'true' else False
        period = request.data.get('period')
        # print(subscription, type(subscription))
        if not amount:
            return Response(status=404)
        if subscription:
            sub = RazorpayClient.create_subscription(amount, period)
            print(amount, sub)
            request.data['id'] = sub['id']
            request.data['plan_id'] = sub['plan_id']
            response = super().post(request, *args, **kwargs)
            response.data['subscription'] = sub
            return response
        else:
            payment = RazorpayClient.create_order(amount)
            print(amount, payment)
            request.data['id'] = payment['id']
            response = super().post(request, *args, **kwargs)
            response.data['payment'] = payment
            return response


class HandleTransactionSuccess(GenericAPIView):

    def post(self, request, *args, **kwargs):
        res = json.loads(request.data["response"])
        ord_id = res.get('razorpay_order_id') or ''
        raz_pay_id = res.get('razorpay_payment_id') or ''
        raz_signature = res.get('razorpay_signature') or ''

        transaction = Transactions.objects.get(id=ord_id)

        data = {
            'razorpay_order_id': ord_id,
            'razorpay_payment_id': raz_pay_id,
            'razorpay_signature': raz_signature
        }

        check = RazorpayClient.verify_payment(data)

        if not check:
            print(data)
            print(check)
            print("Redirect to error url or error page")
            return Response({'error': 'Something went wrong'})

        transaction.is_paid = True
        transaction.save()

        res_data = {
            'message': 'payment successfully received!'
        }

        return Response(res_data)


class HandleSubscriptionPaymentSuccess(GenericAPIView):

    def post(self, request):
        res = json.loads(request.data["response"])
        sub_id = res.get('razorpay_subscription_id') or ''
        raz_pay_id = res.get('razorpay_payment_id') or ''
        raz_signature = res.get('razorpay_signature') or ''

        data = {
            'razorpay_subscription_id': sub_id,
            'razorpay_payment_id': raz_pay_id,
            'razorpay_signature': raz_signature
        }
        sub = Subscription.objects.get(id=sub_id)

        check = RazorpayClient.verify_subscription(data)
        print(data)

        print(check)
        if not check:
            print("Redirect to error url or error page")
            return Response({'error': 'Something went wrong'})
        sub.status = 'active'
        sub.save()
        res_data = {
            'message': 'payment successfully received!'
        }

        return Response(res_data)


class HandleSubscriptionCancel(GenericAPIView):
    def post(self, request):
        pass


class GetTransactionByUser(GenericAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, user):
        data = self.queryset.filter(user=user)
        serializer_obj = self.serializer_class(data, many=True)
        return Response(serializer_obj.data)


class GetSubscriptionByUser(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get(self, request, user):
        data = self.queryset.filter(user=user)
        serializer_obj = self.serializer_class(data, many=True)
        return Response(serializer_obj.data)


class DeleteTransactions(DestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class DeleteSubscription(DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
