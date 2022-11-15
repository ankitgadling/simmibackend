from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
import razorpay
from decouple import config
from .serializers import Transactions, TransactionSerializer
import json
# Create your views here.


class TransactionAPIView(ListCreateAPIView):
    client = razorpay.Client(
        auth=(config('RAZORPAY_KEY'), config('RAZORPAY_SECRET')))
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')

        if not amount:
            return Response(status=404)

        payment = self.client.order.create({"amount": int(amount) * 100,
                                            "currency": "INR",
                                            "payment_capture": "1"})
        request.data['id'] = payment['id']
        response = super().post(request, *args, **kwargs)
        response.data['payment'] = payment
        return response


class HandleTransactionSuccess(GenericAPIView):
    client = razorpay.Client(
        auth=(config('RAZORPAY_KEY'), config('RAZORPAY_SECRET')))

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

        check = self.client.utility.verify_payment_signature(data)

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


class GetTransactionByUser(GenericAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, user):
        data = self.queryset.filter(user=user)
        serializer_obj = self.serializer_class(data, many=True)
        return Response(serializer_obj.data)
