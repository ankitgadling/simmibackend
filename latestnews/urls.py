from django.urls import path
from .views import *


urlpatterns = [
    path('', NewsView.as_view()),
    path('<id>', DetailNewsView.as_view())
]