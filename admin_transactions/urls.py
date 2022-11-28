from django.urls import path
from admin_transactions.views import *




urlpatterns = [
    path('donation/',admin_transactions_view.as_view()),
    path('subscription/',admin_subscription_view.as_view()),
]
