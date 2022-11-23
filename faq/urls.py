from django.urls import path
from .views import *
urlpatterns = [
    path("faqs",FaqView.as_view()),
    path("faq/<pk>",FaqViewDetail.as_view())
]