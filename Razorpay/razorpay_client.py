import razorpay
from decouple import config


class RazorpayClient:
    client = razorpay.Client(
        auth=(config('RAZORPAY_KEY'), config('RAZORPAY_SECRET')))

    @classmethod
    def create_order(cls, amount):
        data = {
            'amount': int(amount)*100,
            'currency': 'INR',
            'payment_capture': 1,

        }
        return cls.client.order.create(data)

    @classmethod
    def verify_payment(cls, params_dict):
        return cls.client.utility.verify_payment_signature(params_dict)

    @classmethod
    def get_plan(cls, amount, period):
        plans = cls.client.plan.all()
        print(amount, period)
        for plan in plans['items']:
            print(plan)
            if plan['item']['amount'] == amount and plan['period'] == period:
                return plan
        return cls.create_plan(amount, period)

    @classmethod
    def create_plan(cls, amount, period):
        amount_text = str(amount)

        data = {
            "period": period,
            "interval": 1,
            "item": {
                "name": f"Simmi Foundation {period} plan of {amount_text} rupees",
                "amount": amount,
                "currency": "INR",
                "description": f"This plan takes {amount_text} {period}"
            },
        }
        plan = cls.client.plan.create(data)
        return plan

    @classmethod
    def create_subscription(cls, amount, period):
        plan = cls.get_plan(int(amount)*100, period)
        count = 50
        data = {
            "plan_id": plan['id'],
            "total_count": count,
            "quantity": 1,
            "customer_notify": 1,
        }
        return cls.client.subscription.create(data)

    @classmethod
    def get_payment_details(cls, payment_id):
        return cls.client.payment.fetch(payment_id)

    @classmethod
    def get_subscription_details(cls, subscription_id):
        return cls.client.subscription.fetch(subscription_id)

    @classmethod
    def verify_subscription(cls, data):
        return cls.client.utility.verify_subscription_payment_signature(data)

    @classmethod
    def cancel_subscription(cls, subscription_id):
        return cls.client.subscription.cancel(subscription_id)
