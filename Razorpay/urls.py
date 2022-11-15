from django.urls import path
from .views import TransactionAPIView, HandleTransactionSuccess, GetTransactionByUser

urlpatterns = [
    path('start-payment/', TransactionAPIView.as_view()),
    path('payment-success/', HandleTransactionSuccess.as_view()),
    path('get-user-transactions/<int:user>/', GetTransactionByUser.as_view()),
]
