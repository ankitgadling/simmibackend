from django.urls import path
from django.contrib import admin
from certifications.views import *



urlpatterns = [
    path('create_cert/',genview.as_view()),
    path('view_cert/',userview.as_view()), 
    path('certificate_base_id/<pk>',certificate_base_id.as_view()), 
    path('view_cert/<id>', uview.as_view()),
    path('cucrts/<str:email>', CurrentUserCertificates.as_view()),
]
