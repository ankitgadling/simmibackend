from django.urls import path
from .views import *

urlpatterns = [
    path("genarate",Genarate.as_view()),
    path('certify',Certify.as_view()),
    path("donation_genarate",Genarate_Donation_Certificate.as_view()),
    ]