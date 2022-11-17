from django.urls import path
from .views import TransactionAPIView, HandleTransactionSuccess, GetTransactionByUser, DeleteTransactions

urlpatterns = [
    path('start-payment/', TransactionAPIView.as_view()),
    path('payment-success/', HandleTransactionSuccess.as_view()),
    path('get-user-transactions/<int:user>/', GetTransactionByUser.as_view()),
    path('delete-transaction/<str:pk>/', DeleteTransactions.as_view()),
]
