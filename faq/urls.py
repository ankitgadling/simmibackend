from django.urls import path
from .views import *
urlpatterns = [
    path("faqs",FaqView.as_view()),
    path("faq/<pk>",FaqViewDetail.as_view()),
    path("popup/",popupuserapi.as_view()),
    path("popupcreate/",popcreateapi.as_view()),
    path("popupcreate/<pk>",popupdateapi.as_view()),
]