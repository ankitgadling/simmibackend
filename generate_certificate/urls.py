from django.urls import path
from .views import *

urlpatterns = [
    path("genarate",Genarate.as_view()),
    path('certify',Certify.as_view()),
    path("donation_genarate/<str:email>",Genarate_Donation_Certificate.as_view()),
    path("subscription_genarate/<str:email>",Genarate_Subscription_Certificate.as_view()),
    path("donation_download",donation_certificate_download.as_view()),
    path("subscription_download",subscription_certificate_download.as_view()),
    path("event_download/<pk>",event_certificate_download.as_view()),
    ]