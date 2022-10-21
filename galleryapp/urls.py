"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from galleryapp.views import *
urlpatterns = [
    path('education',educationapi.as_view()),
    path('education/<pk>',educationapidetail.as_view()),
    path('livelihood',livelihoodapi.as_view()),
    path('livelihood/<pk>',livelihoodapidetail.as_view()),
    path('medical_camps',medical_campsapi.as_view()),
    path('medical_camps/<pk>',medical_campsapidetail.as_view()),
    path('women_empowerment',women_empowermentapi.as_view()),
    path('women_empowerment/<pk>',women_empowermentapidetail.as_view()),
]