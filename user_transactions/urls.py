from django.urls import path
from .views import user_transactionsview
urlpatterns = [
    path('user_transactions/',user_transactionsview.as_view())
]
