from django.urls import path
from admin_transactions.views import *




urlpatterns = [
    path('',admin_transactions_view.as_view()),
]
