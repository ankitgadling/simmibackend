from django.urls import path
from django.contrib import admin
from certifications.views import *
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('create_cert/',genview.as_view()),
    path('view_cert/',userview.as_view()), 
    path('view_cert/<id>', uview.as_view())
]
