from django.urls import path
from .views import *

urlpatterns = [
    path("genarate",Genarate.as_view()),
    path('certify',Certify.as_view())
]