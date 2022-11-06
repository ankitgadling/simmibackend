from django.urls import path
from admin_details.views import *




urlpatterns = [
    path('details',AdmimDetailsView.as_view()),
    path('details/<pk>',AdmimDetailsView2.as_view()),
]
