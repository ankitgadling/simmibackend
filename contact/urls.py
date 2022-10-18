from django.urls import path
from .views import *

urlpatterns= [
    path('contact-us/', contact, name='contact')
]