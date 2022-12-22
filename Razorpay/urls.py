from django.urls import path
from .views import (TransactionAPIView, HandleTransactionSuccess,
                    GetTransactionByUser, DeleteTransactions, HandleSubscriptionPaymentSuccess,
                    HandleSubscriptionCancel, DeleteSubscription, GetSubscriptionByUser)

urlpatterns = [
    path('start-payment/', TransactionAPIView.as_view()),
    path('payment-success/', HandleTransactionSuccess.as_view()),
    path('get-user-transactions/<int:user>/', GetTransactionByUser.as_view()),
    path('delete-transaction/<str:pk>/', DeleteTransactions.as_view()),
    path('subscription-success/', HandleSubscriptionPaymentSuccess.as_view()),
    path('get-user-subscriptions/<int:user>/', GetSubscriptionByUser.as_view()),
    path('delete-subscriptions/<str:pk>/', DeleteSubscription.as_view()),
    path('cancel-subscription', HandleSubscriptionCancel.as_view()),
]
